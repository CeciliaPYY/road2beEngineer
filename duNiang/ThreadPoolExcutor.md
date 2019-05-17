# 4. 线程池的定义、使用方式、启动策略、拒绝策略。ThreadPoolExcutor 构造方法七个参数的含义

## 4.1 线程池 ThreadPoolExcutor 构造方法七个参数的含义
- corePoolSize: 核心池的大小。默认情况下，在创建了线程池之后，线程池中的线程数为 0，当有任务来之后，就会创建一个线程去执行任务，当线程池中的数目达到 corePoolSize，就会把到达的任务放到缓存队列中去；
- maximumPoolSize: 线程池最大线程数，它表示在线程池中最多能创建多少个线程；
- keepAliveTime: 表示线程没有任务执行时最多保持多久时间会终止。默认情况下，只有当线程池中的线程数大于 corePoolSize 时，keepAliveTime 才会起作用，直到线程池中的线程数不大于 corePoolSize，即当线程池中的线程数大于 corePoolSize 时，如果一个线程的空间时间达到 keepAliveTime，则它会被终止，直到线程中的线程数不大于 corePoolSize。但是如果调用了 allowCoreThreadTimeOut(boolean) 方法，在线程池中的线程数不大于 corePoolSize 时，keepAliveTime 参数也会起作用，知道线程池中的线程数为 0；
- unit: 参数 keepAliveTime 的时间单位，有7种取值，在 TimuUnit 类中有7种静态属性；

    - TimeUnit.DAYS;               //天
    - TimeUnit.HOURS;             //小时
    - TimeUnit.MINUTES;           //分钟
    - TimeUnit.SECONDS;           //秒
    - TimeUnit.MILLISECONDS;      //毫秒
    - TimeUnit.MICROSECONDS;      //微妙
    - TimeUnit.NANOSECONDS;       //纳秒

- workQueue: 一个阻塞队列，用来存储等待执行的任务，这个参数的选择也很重要，会对线程池的运行过程产生重大影响，一般来说，这里的阻塞队列有以下几种选择：

    - ArrayBlockingQueue;
    - LinkedBlockingQueue;
    - SynchronousQueue;

其中，ArrayBlockingQueue 和 PriorityBlockingQueue 使用较少，一般使用 LinkedBlockingQueue 和 SynchronousQueue。线程池的排队策略与 BlockingQueue 有关。

- threadFactory: 线程工厂，主要用来创建线程；
- handler: 表示当拒绝处理任务时的策略，有以下四种取值；
    - ThreadPoolExecutor.AbortPolicy: 丢弃任务并抛出RejectedExecutionException异常；
    - ThreadPoolExecutor.DiscardPolicy：也是丢弃任务，但是不抛出异常；
    - ThreadPoolExecutor.DiscardOldestPolicy：丢弃队列最前面的任务，然后重新尝试执行任务（重复此过程）
    - ThreadPoolExecutor.CallerRunsPolicy：由调用线程处理该任务；


## 4.2 ThreadPoolExecutor、AbstractExecutorService、ExecutorService和Executor 之间的关系
- Executor 是一个顶层接口，在它里面是声明了一个方法 execute(Runnable)，返回值为 void，参数为 Runnable 类型，从字面意思可以理解，就是用来执行传进去的任务的；
- ExecutorService 接口继承了 Executor 接口，并声明了一些方法，如 submit、invokeAll、invokeAny 以及shutDown等；
- 抽象类 AbstractExecutorService 实现了 ExecutorService 接口，基本实现了 ExecutorService 中声明的所有方法；
- ThreadPoolExecutor 继承了 AbstractExecutorService 类；

## 4.3 ThreadPoolExecutor 类中几个比较重要的方法
- execute(): 是 Executor 中声明的方法，在 ThreadPoolExecutor 进行了具体的实现，该方法是 ThreadPoolExecutor 的核心方法，通过这个方法可以向线程池提交一个任务，交由线程池去执行；
- submit(): 是 ExecutorService 中声明的方法，在 AbstractExecutorService 中已经有了具体的实现，在 ThreadPoolExecutor 中没有对其进行重写，该方法也是用来向线程池提交任务的，但是它和 execute() 不同在于它能够返回任务执行的结果，去看 submit() 方法的实现，会发现它实际上还是调用 execute()，只不过利用了 Future 来获取任务执行结果；
- shutdown(): 关闭线程池；
- shutdownNow(): 关闭线程池；

此外，还有很多其他的方法，如getQueue() 、getPoolSize() 、getActiveCount()、getCompletedTaskCount()等获取与线程池相关属性的方法，可以自行查阅API。


## 4.4 线程池实现原理
### 4.4.1 线程池状态

- volatile int runState; 
- static final int RUNNING    = 0;
- static final int SHUTDOWN   = 1;
- static final int STOP       = 2;
- static final int TERMINATED = 3;

其中，
- runState: 表示当前线程池的状态，它是一个 volatile 变量来保证线程之间的可见性；
- 当创建线程池后，线程池处于 RUNNING 状态；
- 如果调用了 shutdown() 方法，则线程池处于 SHUTDOWN 状态，此时线程池不能够接受新的任务，它会等待所有任务执行完毕；
- 如果调用了 shutdownNow() 方法，则线程池处于 STOP 状态，此时线程池不能够接受新的任务，并且会去尝试终止正在执行的任务；
- 当线程池处于 SHUTDOWN 或 STOP 状态，并且所有工作线程已经销毁，任务缓存队列已经清空或执行结束后，线程池被设置为 TERMINATED 状态；

### 4.4.2 任务的执行
在了解将任务提交给线程池到任务执行完毕整个过程之前，先来看一下 ThreadPoolExecutor 类中其他的一些比较重要的成员变量

    private final BlockingQueue<Runnable> workQueue; // 任务缓存队列，用来存放等待执行的任务
    private final ReentrantLock mainLock = new ReentrantLock(); // 线程池的主要状态锁，对线程池状态，如线程池大小、RunState 的改变都要使用这个锁
    private final HashSet<Worker> workers = new HashSet<worker>(); // 用来存放工作集
    private volatile long keepAliveTime; // 线程存活时间
    private volatile boolean allowCoreThreadTimeOut; // 是否允许为核心线程设置存活时间；
    private volatile int corePoolSize; // 核心池的大小（即线程池中的线程数目大于这个参数时，提交的任务会被放进任务缓存队列）
    private volatile int maximumPoolSize; // 线程池最大能容忍的线程数
    private volatile int poolSize; // 线程池中当前的线程数
    private volatile RejectedExecutionHandler handler; // 任务拒绝策略
    private volatile ThreadFactory threadFactory;
    // 线程工厂，用来创建线程
    private int largestPoolSize; // 用来记录线程池中曾经出现过的最大线程数
    private long completedTaskCount; // 用来记录已经执行完毕的任务数

对于线程执行过程的总结，
- 如果当前线程池中的线程数目 < corePoolSize，则新来一个任务，就会创建一个线程去执行这一任务；
- 如果当前线程池中的线程数目 >= corePoolSize，则新来一个任务，会尝试将其添加到任务缓存队列中，如果添加成功，则该任务会等待空闲线程将其取出去执行；如果添加失败（一般来说是任务缓存队列已满），则会尝试创建新的线程去执行这个任务；
- 如果当前线程池中的线程数目 = maximumPoolSize，则会采取任务拒绝策略进行处理；
- 如果线程池中的线程数量 >= corePoolSize，且某个线程空闲时间超过 keepAliveTime，线程将被终止，直到线程池中的线程数目不大于 corePoolSize；如果允许为核心池中的线程设置存活时间，那么核心池中的线程空间时间超过 keepAliveTime，线程也会被终止；

### 4.4.3 线程池中线程的初始化
默认情况下，创建线程池后，线程池中是没有线程的，需要提交任务之后才会创建线程。在实际中，如果需要创建线程池的同时立即创建线程，可以通过以下两个方法做到：

- prestartCoreThread()：初始化一个核心线程；
- prestartAllCoreThreads()：初始化所有核心线程

### 4.4.4 任务缓存队列及排队策略
任务缓存队列 workQueue，用来存放等待执行的任务。它的类型为 BlockingQueue<Runnable>，通常有下面三种类型：

- ArrayBlockingQueue: 基于数组的先进先出队列，创建时需要指定大小；
- LinkedBlockingQueue: 基于链表的先进先出队列，如果创建时没有制定大小，则默认为 Integer.MAX_VALUE；
- synchronousQueue: 这个队列比较特殊，它不会保存提交的任务，而是将直接新建一个线程来执行新来的任务；

### 4.4.5 线程池容量的动态调整
ThreadPoolExecutor 提供了动态调整线程池容量大小的方法。

- setCorePoolSize(): 设置核心池大小
- setMaximumPoolSize(): 设置线程池最大能创建的线程数目大小

### 4.4.6 注意
在 java doc 中，不提倡我们直接使用  ThreadPoolExecutor，而是使用 Executors 类中提供的几个静态方法来创建线程池，

    Executors.newCachedThreadPool();        //创建一个缓冲池，缓冲池容量大小为Integer.MAX_VALUE
    Executors.newSingleThreadExecutor();   //创建容量为1的缓冲池
    Executors.newFixedThreadPool(int);    //创建固定容量大小的缓冲池

从他们的具体实现来看，它们实际上也是调用了ThreadPoolExecutor，只不过参数都已配置好了。
其中，
- newCachedThreadPool 将 corePoolSize 设置为 0，将 maximumPoolSize 设置为 Integer.MAX_VALUE，使用的 synchronousQueue，也就是说来了任务就创建线程运行，当线程空闲超过60秒，就销毁线程；
- newSingleThreadExecutor 将 corePoolSize 和 maximumPoolSize 都设置为1，使用的 LinkedBlockingQueue；
- newFixedThreadPool 创建的线程池 corePoolSize 和 maximumPoolSize 值是相等的，它使用的 LinkedBlockingQueue；

### 4.4.7 如何合理配置线程池的大小
一般需要根据任务的类型来配置线程池的大小：

- 如果是 CPU 密集型任务，就需要尽量压榨 CPU，参考值可以设为 (CPU 数量 + 1);
- 如果是 IO 密集型任务，参考值可以设置为 2 * (CPU 数量)；

当然这只是一个参考值，具体的设置还需要根据实际情况进行调整，比如可以先将线程池大小设置为参考值，再观察任务运行情况和系统负载、资源利用率来适当调整。








