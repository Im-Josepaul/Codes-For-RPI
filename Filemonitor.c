#include <stdio.h>
#include <stdlib.h>
#include <sys/inotify.h>

#define MAX_EVENT_MONITOR 2048
#define NAME_LEN 32 //filename length
#define MONITOR_EVENT_SIZE (sizeof(struct inotify_event)) //size of one event
#define BUFFER_LEN MAX_EVENT_MONITOR*(MONITOR_EVENT_SIZE + NAME_LEN) //buffer length

int main (int argc, char** argv)
{
    int fd, watch_desc;
    char buffer[BUFFER_LEN];
    fd = inotify_init();
    if(fd<0)
    {
        perror("Notify not initialized");
    }
    watch_desc = inotify_add_watch(fd,"/home/pi/Desktop/Codes-For-RPI",IN_CREATE|IN_MODIFY);
    if(watch_desc == -1)
    {
        printf("Could'nt add watch to %s\n","/home/pi/Desktop/Codes-For-RPI");
    }    

    int i=0;
    while(1)
        {
            i=0;
            int total_read = (fd,buffer,BUFFER_LEN);
            if (total_read < 0)
            {
                perror("Read Error");
            }
            while (i < total_read)
            {
                struct inotify_event *event=(struct inotify_event)&buffer[i];
                if (event->len)
                {
                    
                }
                
            }
            
        }
    }

}