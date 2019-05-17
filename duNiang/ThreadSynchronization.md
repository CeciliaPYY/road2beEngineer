# 3. 线程间的同步
## 3.1 需要进行同步的原因
java 允许多线程并发控制，当多个线程同时操作一个可共享的资源变量时，将会导致数据不准确，相互之间产生冲突，因此加入同步锁以避免在该线程没有完成操作之前，被其他线程的调用， 从而保证了该变量的唯一性和准确性。

## 3.1 七类线程间的同步方法
### 3.1.1 同步方法
即有 synchronized 关键字修饰的方法。由于 java 的每个对象都有一个内置锁，当用此关键字修饰方法时，内置锁会保护整个方法。在调用该方法前，需要获得内置锁，否则就处于阻塞状态。

    public synchronized void save(){}

### 3.1.2 同步代码块
即有 synchronized 关键字修饰的代码块。被该关键词修饰的语句块会被自动加上内置锁，从而实现同步。

    synchronized(object){ 
    }
    // note:同步是一种高开销的操作，因此应该尽量减少同步的内容。通常没有必要同步整个方法，使用synchronized代码块同步关键代码即可。 

### 3.1.3 使用特殊域变量 volatile 实现线程同步
- volatile 关键字为域变量的访问提供了一种免锁机制；
- 使用 volatile 修饰域相当于告诉虚拟机该域可能被其他线程更新；
- 因此每次使用该域就要重新计算，而不是使用寄存器的值；
- volatile 不会提供任何原子操作，它也不能用来修饰 final 类型的变量；

note: 原子操作（atomic operation）是不需要 synchronized。所谓原子操作是指不会被线程调度机制打断的操作；这种操作一旦开始，就一直运行到结束，中间不会有任何 context switch（切换到另一个线程）。

    //只给出要修改的代码，其余代码与上同
        class Bank {
            //需要同步的变量加上volatile
            private volatile int account = 100;

            public int getAccount() {
                return account;
            }
            //这里不再需要synchronized 
            public void save(int money) {
                account += money;
            }
        ｝

note: 多线程中的非同步问题主要出现在对域的度协商，如果让域本身避免这个问题，则不需要修改操作该域的方法。用 final域，有锁保护的域和 volatile域可以避免非同步的问题。

### 3.1.4 使用重入锁实现线程同步
在 JavaSE 5.0 中新增了一个 java.util.concurrent 包来支持同步。ReentrantLock 类是可重入、互斥、实现了 Lock 接口的锁，它同使用 synchronized 关键字的方法和代码块具有相同的基本行为和语义，并扩展了其能力。

ReentrantLock 类的常用方法：
- ReentrantLock() : 创建一个ReentrantLock实例 
- lock() : 获得锁 
- unlock() : 释放锁 

        //只给出要修改的代码，其余代码与上同
        class Bank {
        
        private int account = 100;
        //需要声明这个锁
        private Lock lock = new ReentrantLock();
        public int getAccount() {
            return account;
        }
        //这里不再需要synchronized 
        public void save(int money) {
            lock.lock();
            try{
                account += money;
            }finally{
                lock.unlock();
            }
            
        }
        ｝
note: 关于 Lock 对象和 synchronized 关键字的选择
- 最好两个都不用，使用一种java.util.concurrent包提供的机制， 能够帮助用户处理所有与锁相关的代码。 
- 如果synchronized关键字能满足用户的需求，就用synchronized，因为它能简化代码 
- 如果需要更高级的功能，就用ReentrantLock类，此时要注意及时释放锁，否则会出现死锁，通常在finally代码释放锁 


### 3.1.5 使用局部变量实现线程同步
如果使用 TreadLocal 管理变量，则每一个使用该变量的线程都获得该变量的副本，副本之间相互独立，这样每一个线程都可以随意修改自己的变量副本，而不会对其他线程产生影响。

TreadLocal 类的常用方法
- TreadLocal()：创建一个线程本地变量；
- get(): 返回此线程局部变量的当前线程副本中的值；
- initialValue() : 返回此线程局部变量的当前线程的"初始值" 
- set(T value) : 将此线程局部变量的当前线程副本中的值设置为value

note: ThreadLocal 与同步机制
- 二者都是为了解决多线程中相同变量的访问冲突问题；
- 前者采用以“空间换时间”的方法，后者采用以“时间换空间”的方式


### 3.1.6 使用阻塞队列实现线程同步
前面提到的方法都是在底层实现的线程同步，但是在实际开发中，应当尽量原理底层结构。使用 javaSE 5.0版本中新增的 java.util.concurrent 包将有助于简化开发。
本小节主要是使用 LinkedBlockingQueue<E> 来实现线程的同步，LinkedBlockingQueue<E> 是一个基于已连接节点的，范围任意的 Blocking Queue。队列是先进先出的顺序（FIFO）。

LinkedBlockingQueue 类常用方法
- LinkedBlockingQueue() : 创建一个容量为Integer.MAX_VALUE的LinkedBlockingQueue 
- put(E e) : 在队尾添加一个元素，如果队列满则阻塞 
- size() : 返回队列中的元素个数 
- take() : 移除并返回队头元素，如果队列空则阻塞

note: BlockingQueue<E>定义了阻塞队列的常用方法，尤其是三种添加元素的方法，我们要多加注意，当队列满时：
- add()方法会抛出异常
- offer()方法返回false
- put()方法会阻塞

### 3.1.7 使用原子变量实现线程同步
需要线程同步的根本原因在于对普通变量的操作不是原子的。
对于原子操作的定义如下，原子操作就是指将读取变量值、修改变量值、保存变量值看成一个整体来操作即这几种行为要么同时完成，要么都不完成。

在 java 的 util.concurrent.atomic 包中提供了创建原子类型变量的工具类，使用该类可以简化线程同步。

其中AtomicInteger 表可以用原子方式更新int的值，可用在应用程序中(如以原子方式增加的计数器)，
但不能用于替换Integer；可扩展Number，允许那些处理机遇数字类的工具和实用工具进行统一访问。

AtomicInteger类常用方法：
- AtomicInteger(int initialValue) : 创建具有给定初始值的新的AtomicInteger
- addAddGet(int dalta) : 以原子方式将给定值与当前值相加
- get() : 获取当前值

        class Bank {
                private AtomicInteger account = new AtomicInteger(100);

                public AtomicInteger getAccount() {
                    return account;
                }

                public void save(int money) {
                    account.addAndGet(money);
                }
            }

note: 原子操作主要有
- 对于引用变量和大多数原始变量（long 和 double 除外）的读写操作；
- 对于所有使用 volatile 修饰的变量（包括 long 和 double）的读写操作；