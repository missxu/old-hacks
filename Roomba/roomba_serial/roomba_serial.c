#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <termios.h>
#include <unistd.h>
#include <sys/select.h>

#define SYSCALL(A) do { ret = A; if (ret == -1) { perror(#A); return -1; } else printf("%s returned %d\n", #A, ret); } while (0)
int ret; /* necessary for SYSCALL */

#define SERIAL_PORT "/dev/cu.usbserial-AI02KGID"

#define WAIT_FLAG_READ 1
#define WAIT_FLAG_WRITE 2

int setup_terminal(int fd) {
    struct termios tio;
    int ret;
    SYSCALL(tcgetattr(fd, &tio));

    cfmakeraw(&tio);

    tio.c_cflag = CS8|CREAD|CLOCAL;
    tio.c_cc[VMIN] = 1;
    tio.c_cc[VTIME] = 1;

    cfsetispeed(&tio, B115200);
    cfsetospeed(&tio, B115200);

    SYSCALL(tcsetattr(fd, TCSANOW, &tio));
    return ret;
}

int wait_data(int fd, int wait_flags) {
    fd_set rfds, wfds, xfds;
    struct timeval to;

    to.tv_sec = 1;
    to.tv_usec = 0;

    FD_ZERO(&rfds);
    FD_ZERO(&wfds);
    FD_ZERO(&xfds);
    if (wait_flags & WAIT_FLAG_READ) FD_SET(fd, &rfds);
    if (wait_flags & WAIT_FLAG_WRITE) FD_SET(fd, &wfds);
    FD_SET(fd, &xfds);

    int ret = select(fd+1, &rfds, &wfds, &xfds, &to);
    if (ret == -1) perror("select");
    else if (ret > 0)
    {
        if(FD_ISSET(fd, &rfds))
            puts("Ready to read");
        if(FD_ISSET(fd, &wfds))
            puts("Ready to write");
        if(FD_ISSET(fd, &xfds))
            puts("Exception!");
    }
    else puts("Timed out!");
    return 0;
}

int main(int argc, char **argv)
{
    char buf[256];
    int fd = open(SERIAL_PORT, O_RDWR | O_NOCTTY | O_NONBLOCK);
    int read_bytes;
    int i;
    int ret;

    setup_terminal(fd);

    wait_data(fd, WAIT_FLAG_WRITE);

    for (i = 1; i < argc; i++) {
        unsigned char c = atoi(argv[i]);
        SYSCALL(write(fd, &c, 1));
    }

    wait_data(fd, WAIT_FLAG_READ);
    read_bytes = read(fd, buf, sizeof(buf));
    printf("Read %d bytes:\n", read_bytes);
    for (i = 0; i < read_bytes; ++i) {
         printf("%02x ", buf[i]);
    }
    printf("\n");
    close(fd);

    return 0;
}
