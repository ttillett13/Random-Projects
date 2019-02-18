#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
    char buf[100];
    int rc = read(0, buf, sizeof(buf));
    printf("%s", buf);
    printf("buf complete\n");
    return 0;
}
