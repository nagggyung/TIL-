## Study from Deep lizard - lecture: Neural Network Programming - Deep Learning with PyTorch

### chap2. PyTorch Explained - Python Deep Learning Neural API

PyTorch is a Deep Learning framework and a scientific computing package. The scientific computing aspect of Pytorch is primarily a result Pytorch's tensor library and associated tensor operations. 

* A tensor is an n-dimensional array

For now, just know that PyTorch tensors and their associated operations are very similar to numpy n-dimensional arrays.
Tensors are super important for deep learning and neural networks because they are the data structure that we ultimately use for building and training our neural networks.

### why use PyTorch for deep learning?
* PyTorch is thin and stays out of the way
* PyTorch is as close as it gets to the real thing.

### chap 4. CUDA Explained- why Deep Learning uses GPUs
The goal of this post is to help beginners understand what CUDA is and how it fits in which PyTorch, and more importantly, why we even use GPUs in neural network programming.

### Graphics Processing Unit(GPU)
A GPU is a processor that is good at handling specialized computations.
This is in contrast to a central processing unit(CPU), which is a processor that is good at handling general computations.

A GPU can be much faster at computing than a CPU. However, this is not always the case.
The speed of a GPU relative to a CPU depends on the type of computation being performed.
The type of computation most suitable for a GPU is a computation that can be done in parallel.

### Parallel Computing
Parallel computing is a type of computation where by a particular computation is broken into independent smaller computations that can be carried out simulataneoulsy.
The resulting computations are then recombined or synchronized, to form the result of the original larger computation.

The number of tasks that a larger task can be broken into depends on the number of cores contained on a particular piece of hardware. Cores are the units that actually do the computation within a given processor, and CPUs typically have four, eight or sixteen cores while GPUs have potentially thousands.

We can conclude that parallel computing is done using GPUs, and we can also conclude that tasks which are best suited to be solved using a GPU are tasks that can be done in parallel, we can accelerate our computation using parallel programming approaches and GPUs. 

### Neural Networks Are Embarrassingly Parallel 

Many of the computations that we do with neural networks can be easily broken into smaller computations in such a way that the set of smaller computations do not depend on one another. One such example is a convolution.

### Pytorch comes with CUDA

One of the benefits of using PyTorch, or any other neural network API is that parallelism comes baked into the API. This means that as neural network programmers, we can focus more on building neural networks and less on performance issuses.

### Using CUDA with PyTorch

If we want a particual computation to be performed on the GPU, we can instruct PyTorch to do so by calling 'cuda()' on our data structures (tensors)

suppose we have the following code:
   * t = torch.tensor([1,2,3])

The tensor object created in this way is on the CPU by default.
As a result, any operations that we do using this tensor object will be carried out on the CPU.

Now, to move the tensor onto the GPU, we just write:

  * t = t.cuda()
  * t
  tensor([1,2,3], device = 'cuda: 0')

This ability makes PyTorch very versatile because computations can be selectively carried out either on the CPU or on the GPU.

### GPGPU Computing 

Deep learning along with many other scientific computing tasks that use parallel programming techniques are leading to a new type of programming model called GPGPU or general purpose GPU computing.

GPGPU computing is more commonly just called GPU computing or accelerated computing now that it's becoming more common to perform a wide variety of tasks on a GPU. 



