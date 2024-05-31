# 帮助
- [KVM之五：KVM日常管理常用命令](https://www.cnblogs.com/chenjiahe/p/5919426.html)
- [KVM 操作虚拟机常用命令](https://blog.csdn.net/wh211212/article/details/74908390)
- [[ kvm ] 学习笔记 7：KVM 虚拟机创建的几种方式](https://www.cnblogs.com/hukey/p/11307129.html)

# 一些知识
### KVM-Qemu-Libvirt三者之间的关系
- link
    - https://blog.51cto.com/changfei/1672147
- Qemu 是一个模拟器，它向Guest OS模拟CPU和其他硬件，Guest OS认为自己和硬件直接打交道，其实是同Qemu模拟出来的硬件打交道，Qemu将这些指令转译给真正的硬件。
- KVM 是linux内核的模块，它需要CPU的支持（CPU支持 硬件辅助虚拟化技术Intel-VT，AMD-V，内存的相关如Intel的EPT和AMD的RVI技术）Guest OS的CPU指令不用再经过Qemu转译，直接运行；所以效率相比把命令转译一遍的Qemu要高， 但因为其本身只能提供CPU和内存的虚拟化， 所以它必须结合QEMU才能构成一个完成的虚拟化技术，这就是下面要说的qemu-kvm。
- qemu-kvm 将有关CPU指令的部分交由内核模块来做。kvm负责cpu虚拟化+内存虚拟化， 但因为kvm不能模拟其他设备，所以用qemu模拟IO设备（网卡，磁盘等）。kvm加上qemu之后就能实现真正意义上服务器虚拟化。
- libvirt libvirt是目前使用最为广泛的对KVM虚拟机进行管理的工具和API。Libvirtd是一个daemon进程，可以被本地的virsh调用，也可以被远程的virsh调用，Libvirtd调用qemu-kvm操作虚拟机。

# 名词
- Inter VT http http哈
    - VT(Virtualization Technology) 
    - Intel VT就是指Intel的虚拟化技术。这种技术简单来说就是可以让一个CPU工作起来就像多个CPU并行运行，从而使得在一台电脑内可以同时运行多个操作系统(如Vmware WorkStation)。只有部分Intel 的CPU才支持这种技术。
    - 是为解决纯软件虚拟化解决方案在可靠性、安全性和性能上的不足