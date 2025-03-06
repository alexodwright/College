The purpose of this lab was to explore Docker technology by running a performance-sensitive application inside a Docker container and comparing the performance results against a Virtual Machine.

## Docker

Docker is an open-source platform that automates the managements of containers.

Containers virtualize the operating system without requiring dedicated hardware as they share the same kernel of the hosting system. They present the impression of a separate OS but since they're sharing the kernel, they are much lighter than a virtual machine.

Container image sizes are much smaller than the image size for a VM. The boot time is around 10 times faster than the boot time of the VM so dockers are must faster at booting up than a VM. However due to the nature of a container, it is less secure as it is running on the same kernel as the host machine. VM's use virtual hardware and are completely separate from the host machine making them more secure.

## Steps to run the application in the Docker:

1. Since my machine runs Arch Linux I installed Docker Desktop through the package manager 'yay' using the command `yay -S docker-desktop`
2. Once installed and running I created a new directory for my docker image and created the Dockerfile which looked like this:

```Dockerfile
# Using the same Ubuntu Image as I did for Lab 4
FROM ubuntu:24.04

# install python
RUN apt-get update && apt-get install -y python3

# copy the stress_test.py from my host machine into the docker container
COPY stress_test.py /app/stress_test.py

# change the working directory to the 'app' directory where the python file
# is stored
WORKDIR /app
# run the python file
CMD ["python", "stress_test.py"]
```

3. My python file was as follows - (I removed the matplotlib module as I printed the values of n and the executions to the log terminal so I could graph the results on the host machine. Since the docker container does not provide a GUI of the graph.):

```Python
# purpose of this file is to stress test a docker container and to also compare the runtimes to a VM

# imports
import numpy as np
import time

def stress_test(n) -> None:
    # create two matrices of n size
    a = np.random.rand(n, n)
    b = np.random.rand(n, n)

    # get the start time
    start_time = time.time()

    # multiply the matrices together
    c = np.matmul(a, b)

    # get the end time and the total execution time
    end_time = time.time()
    exec_time = end_time - start_time
    exec_time *= 1000

    return exec_time

def main() -> None:
    n_values = []
    exec_times = []

    # run the simulation 1-150 times
    for n in range(1, 151):
        n_values.append(n)
        exec_times.append(stress_test(n))

    print(n_values)
    print()
    print(exec_times)

if __name__ == "__main__":
    main()
```

4. I then ran the command: `docker built -t lab5dockerimg .` which searched the current directory for a docker file and builds an image from it with the name 'lab5dockerimg'.
5. Once the build was complete I navigated to the images section of Docker Desktop where I selected the new image and clicked 'Run'.
6. This opened a dialog box to create the container, so I gave it a name 'lab5container' and ran the container.
7. I then navigated to the container details screen that appeared like the following screenshot: 
   ![[Pasted image 20241118223239.png]]
8. I then retrieved the values for n and the executions time from the logs and plotted them on a graph using matplotlib on my host machine.

The graph appeared as follows:

### Docker Results
![[Results.png]]

## Comparative Analysis

The results from running the program on the VM were as follows:

### VM Results
![[VM.png]]

Similar to the results from Lab 4, in my experience the Virtual Machine runs faster than the docker container. This is unusual as containers are more lightweight and reduce resource usage compared to Virtual Machines since they share the same OS of the host machine. Docker containers also have minimal overhead, which allow applications and scripts to run closer to the bare-metal performance.

We can see that the container peaked almost 3 times as high as the VM with the peak of the container being around 1.4ms and the peak of the VM being around .4ms. It also appears that the container spiked much more than the VM's smoother graph.

An explanation for the performance difference could be that the VM was allocated more resources than the container which resulted in the difference in performance. Furthermore due to the VM's isolated nature it could have potentially more optimized I/O subsystems. The overhead of managing the docker containers could also have led to the reduction of performance.

## Reflection on Docker experience

My experience with the docker technology was quite smooth and simple with no major problems. From this Lab I learned with hands on experience how to implement and create containers and images and learned how the Dockerfile is laid out. I also developed my understanding of container layers and how they can be shared between docker images.