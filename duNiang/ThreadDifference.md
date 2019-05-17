# 2. extends Thread 和 implement Runnable 差异在哪里 
## 问题背景
在安卓中 Handler 消息传递机制中，创建新线程有两种方式，一种是实现 Runnable 接口，即 implement Runnable ；而另一种则是继承 Thread 类，即 extends Thread 。那这两种方法之间有什么差异呢？

## 代码示例
    public class ThreadA implements Runnable {
        public void run() {
            //Code
        }
    }
    //调用 "new Thread(threadA).start()" 来开启线程

    public class ThreadB extends Thread {
        public ThreadB() {
            super("ThreadB");
        }
        public void run() {
            //Code
        }
    }
    //调用 "threadB.start()" 来开启线程

## 不同之处
- 由于 Java 是单继承机制，不允许同时继承多个类。因此，当继承了 Thread 类之后，就不能再继承其他类了。而实现 Runnable 接口则不一样，还可以继承其他类；
- 当继承 Thread 类是，每一个 Thread 对象创造不同的对象然后关联它们，而实现 Runnable 接口则不一样，是多个线程共享一个对象。（需要加上 synchronized 关键字）

    ||继承 Thread 类|  实现 Runnable 接口 |
    |--------| -----:|:----:|
    |是否可以继承其他类|否|是|
    |是否共享对象|否|是|

    note: 实现 Runnable 接口进行资源共享时，synchronized 关键字可只用于方法体，而继承 Thread 类也可以进行资源共享，此时需要对 class 添加 synchronized 关键字 以及 static 关键字。
    
## 总结
当你想要在一组线程中访问相同的资源时，使用Runnable接口。在这种情况下要避免使用Thread类，因为多对象的创建会占用更多的内存，会导致大的性能花费。此外，Thread类内部实现了Runnable接口。

