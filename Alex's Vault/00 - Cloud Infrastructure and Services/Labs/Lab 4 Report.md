
## Task 1: Application Development

```python
# purpose of this file is to stress test a VM and to also compare the runtimes on different machines

# imports
import numpy as np
import time
import matplotlib.pyplot as plt

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

    # create a figure and plot the results against n
    fig, ax = plt.subplots()
    ax.plot([n for n in n_values], [t for t in exec_times])
    plt.xlabel("Value of n")
    plt.ylabel("Execution time in ms")
    plt.title("Execution time vs N")
    plt.show()

if __name__ == "__main__":
    main()
```

On the host machine this was the graph I obtained:

### Host Machine
![[HostMachine.png]]

## Task 2: Virtual Machine Setup and Configuration

I used VirtualBox to configure my VM. I also used Ubuntu Version 24.04.1 as the operating system. I configured the VM with 8GB of RAM and 4 CPU processors.

The operating system of the host machine is Arch Linux. With a 12th Generation Intel i5-1240P processor running at 4.4 GHz AND 16GB of RAM.

### Host Machine Specs:
![[Pasted image 20241116215932.png]]

### Virtual Machine Specs:
![[VM-Specs.png]]

## Task 3: Running the Application in the Virtual Machine

This is the graph I obtained using the Virtual Machine with the same script as above in Task 1:

### Virtual Machine
![[VM.png]]

## Task 4: Report Compilation

Analysis:

From the graphs it was interesting to see that the stress test ran almost twice as quick on the VM as it did on the host machine.

This was the RAM usage for python while running the script on the VM:
![[VMBtop.png]]
As we can see here at the first row, python3 is using 176MB of RAM.

This was the RAM usage for Python while running the script on the host machine:
![[HostBTOP.png]]

As we see here at the third row, Python is using 114MB of RAM which is 62MB less or about 2/3rds of the RAM being used in the VM.

After doing some research this seems to be a common scenario with the main reasoning behind being that the VM is much less cluttered and more optimized and can therefore run the script better. Another reason I found was that the host machine has real hardware that respond to the OS while the VM has virtual hardware that responds in a fraction of the time.

### Setting up of the Virtual Machine

My experience of setting up the virtual machine using VirtualBox was quite smooth and I encountered no challenges. After following the tutorial it was easy to setup and configure the VM with the resources I wanted and it booted up straight away with no issues. I gained insights into the reasoning and setup of virtual machines. I understand more why virtual machines are used to simulate an environment, as is able to be used for testing without the repercussions of making mistakes like on a host machine. They can also be used to create a uniform working environment for an application or program.

