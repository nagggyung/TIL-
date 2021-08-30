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

### Using CUDA With PyTorch

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

### Chap5. Tensors Explained - Data Structures Of Deep Learning

### What is a Tensor?

The inputs, outputs, and transformations within neural networks are all represented using tensors, and as a result, neural network programming utilizes tensors heavily.

* A Tensor is the primary data structure used by neural networks.

### Specific instances of Tensors

Each of these examples are specific instances of the more general concept of a Tensor:
* number
* scalar
* array
* vector
* 2d-array
* matrix

In Deep Learning, we usually just refer to all these as tensors.

### Indexes Required To Access An Element

The relationship within each of these pairs is that both elements require the same number of indexes to refer to a specific element within the data structure.
 
![image](https://user-images.githubusercontent.com/74478432/129898971-674415c1-00ed-4104-b5d7-76f6bf41cf9d.png)

### Tensors are generalizations

Tensors are multidimensional arrays or nd-arrays for short. The reason we say a tensor is a generalization is because we use the word tensor for all values of n like so:

* A scalar is a 0 dimensional tensor
* A vector is a 1 dimensional tensor
* A matrix is a 2 dimensional tensor
* A nd-array is an n dimensional tensor

### Chap6. Rank, Axes, And Shape Explained - Tensors For Deep Learning

### Rank of a Tensor

The Rank of a tensor refers to the number of dimensions present within the tensor.
Suppose we are told that we have a rank-2 tensor. This means all of the following:

* We have a matrix 
* We have a 2d-array
* We have a 2d-tensor

### Rank and indexes

A tensor's rank tells us how many indexes are needed to access a specific element within the tensor.

### Axes of a Tensor

An axis of a tensor is a specific dimension of a tensor. If we say that a tensor is a rank-2 tensor, we mean that the tensor has 2 dimensions, or equivalently, the tensor has two axes.

### Length of An Axis

The length of each axis tells us how many indexes are available along each axis.

### Shape of a Tensor

The shape of a tensor is determined by the length of each axis, so if we know the shape of a given tensor, then we know the length of each axis, and this tells us how many indexes are available along each axis.

The shape of a tensor gives us the length of each axis of the tensor:

You can get the shape of a tensor by writing 't.shape'. In PyTorch, size and shape of a tensor are the same thing.

### Reshaping a Tensor

![2021-08-19 (13)](https://user-images.githubusercontent.com/74478432/130089193-c05d542d-b1ed-4dd2-93b7-221cfc1a05a9.png)

![2021-08-19 (12)](https://user-images.githubusercontent.com/74478432/130089206-b1958b85-4145-4a1e-9ff5-fd58e865907e.png)

Now, one thing to notice about reshaping is that the product of the component values in the shape must equal the total number of elements in the tensor.

For example, 
* 3 x 3 = 9
* 1 x 9 = 9


### Chap 7. CNN Tensor Shape Explained - Convolutional Neural Networks And Feature Maps

### Convolutional Neural Network 

What I want to do now is put the concepts of rank, axes, and shape to use with a practical example. To do this, we'll consider an image input as a tensor to a CNN.
Remember that the shape of a tensor encodes all the relevant information about a tensor's axes, rank, and indexes, so we'll consider the shape in our example.

### Shape of CNN Input

The shape of a CNN input typically has a length of four. This means that we have a rank-4 tensor with four axes. Each index in the tensor's shape represents a specific axis, and the value at each index gives us the length of the corresponding axis.

* (A,B,C,D) : rank-4 tensor = 4 axes

For images, the raw data comes in the form of pixels that are represented by a number and are laid out using two dimensions, height and width.

### Image data in tensor

* (Batch, Channels, Height, Width)

### Feature Maps

Feature maps are the output channels created from the convolutions. 

The word "feature" is used because the outputs represent particular features from the image, like edges for example, and these mappings emerge as the network learns during the training process and become more complex as we move deeper into the network.

### Chap8. PyTorch Tensors Explained - Neural Network Programming
### Introducing PyTorch Tensors
PyTorch tensors are the data structures we'll be using when programming neural networks in PyTorch. When programming neural networks, data preprocessing is often one of the first steps in the overall process, and one goal of data preprocessing is to transform the raw input data into tensor form.

### Instances of the torch.Tensor class

PyTorch tensors are instances of the torch.Tensor Python class. We can create torch.Tensor object using the class constructor like so:
![2021-08-24 (12)](https://user-images.githubusercontent.com/74478432/130637066-28d73c91-8f64-4753-a6b2-d017b0034164.png)

This creates an empty tensor(tensor with no data).

### Tensor Attributes 
Every torch.Tensor has these attribute values:
* torch.dtype
* torch.device
* torch.layout

### PyTorch Tensor Type Promotion
Arithmetic and comparison operations, as of PyTorch version 1.3, can perform mixed-type operations that promote to a common dtype. The example below was not allowed in version 1.2. However, in version 1.3 and above, the same code returns  tensor with dtype = torch.float32

![2021-08-24 (13)](https://user-images.githubusercontent.com/74478432/130638353-15f6bb7b-4209-4885-b165-c7c56275505f.png)

### Tensors Have A torch.device
The device, CPU in our case, specifies the device(CPU or GPU) where the tensor's data is allocated. This determines where tensor computations for the given tensor will be performed. PyTorch supports the use of multiple devices, and they are specified using an index like so:

![2021-08-24 (16)](https://user-images.githubusercontent.com/74478432/130639027-638aa5b2-7aea-4ee7-8e8d-e3afba5cce2d.png)


One thing to keep in mind about using multiple devices is that tensor operations between tensors must happen between tensors that exist on the same device. 

### Tensors Have A torch.layout
The layout, strided in our case, specifies how the tensor is stored in memory 

### Take Away From The Tensor Attributes 
As neural network programmers, we need to be aware of the followings:
* Tensors contain data of a uniform type (dtype)
* Tensor computations between tensors depend on the dtype and the device

### Creating Tensors Using Data
These are the primary ways of creating tensor objects (instances of the torch.Tensor class), with data(array-like) inb PyTorch.

* torch.Tensor(data)
* torch.tensor(data)
* torch.as_tensor(data)
* torch.from_numpy(data)

![2021-08-30](https://user-images.githubusercontent.com/74478432/131357314-36d2a59c-db6d-407b-a642-c88138db4850.png)

All the options (o1, o2, o3, o4) appears to have produced the same tensors except for the first one. The first option (o1) has dots after the number indicating that the numbers are floats, while the next three options have a type of int32.


### Creating Options Without Data
* torch.eye(): returns a 2-D tensor with ones on the diagonal and zeros elsewhere.
* torch.zeros(): creates a tensor of zeros with the shape of specified shape argument.
* torch.ones(): creates a tensor of ones.
* torch.rand(): creates a tensor with a shape of the specified argument whose values are random.

