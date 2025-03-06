#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

int main() {
    
    int fd;
    char buff[80];

    // open file
    FILE *file = fopen("sensor_data.csv", "r");
    if (file == NULL) {
        printf("Error opening the file!\n");
        return 1;
    }
    char * fifo = "/tmp/fifo";

    // create the pipe
    mkfifo(fifo, 0666);

    // read file line by line and write to pipe
    //close the file, close the pipe
    while (fgets(buff, 1000, file) != NULL) {
        fd = open(fifo, O_WRONLY);
        write(fd, buff, strlen(buff)+1);
        close(fd);
    }

    return EXIT_SUCCESS;
}