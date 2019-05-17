# 1. 如何创建使用线程 Thread 
## 1. new Thread
    new Thread(new Runnable() {

        @Override
        public void run() {
            // TODO Auto-generated method stub
            }
        }
    ).start();

- 每次 new Thread 新建对象性能差；
- 线程缺乏统一管理，可能无限制新建线程，相互之间竞争，及可能占用过多系统资源导致死机或oom；
- 缺乏更多功能，如定时执行、定期执行、线程中断；

## 2. Java 线程池
### 2.1. 线程池的类别
Java Executors 提供了 4 种线程池，分别是

- newCachedThreadPool 创建一个可缓存线程池，如果线程池长度超过处理需要，可灵活回收空闲线程，若无可回收，则创建线程；
- newFixedThreadPool 创建一个定长线程池，可控制线程最大并发数，超出的线程会在队列中等待；
- newScheduledThreadPool 创建一个定长线程池，支持定时及周期性任务执行；
- newSingleThreadExecutor 创建一个单线程化的线程池，它只会用唯一的工作线程来执行任务，保证所有任务按照指定顺序（FIFO，LIFO，优先级）执行。

### 2.2. 线程池的作用
- 限制系统中执行线程的数量；

### 2.3. 使用线程池的原因
- 减少了创建和销毁线程的次数，每个工作线程都可以被重复利用，可执行多个任务；
- 可根据系统的承受能力，调整线程池中的工作线程数目；

### 2.4. 线程池中比较重要的类
- ExecutorService：真正的线程池接口；
- ScheduledExecutorService：解决那些需要任务重复执行的问题；
- ThreadPoolExecutor：ExecutorService的默认实现；
- ScheduledThreadPoolExecutor：继承ThreadPoolExecutor 的 ScheduledExecutorService 接口实现，周期性任务调度的类实现；



