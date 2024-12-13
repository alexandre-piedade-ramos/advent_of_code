#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
struct darr{
    void * data;
    size_t size;
    size_t len;
};

void append(uint64_t * arr, size_t * len, size_t * sz, uint64_t * val){
    if(*len==*sz) arr = realloc(arr,*sz*2);
    arr[*len-1]=*val;
}

uint64_t countDigits(uint64_t val){
    uint64_t n=0;
    while((val>>n++)>0);
    return n;
}

int main(int argc, char * argv[]){
    char start[1024];
    int num=0,len=0,pos=0,size=512;
    if(argc<3){perror("olha os args\n");return 1;}
    FILE* inf=fopen(argv[1],"r");
    size_t blinks=atoi(argv[2]);
    uint64_t *vals=calloc(size,sizeof(uint64_t));
    fgets(start,1024,inf);
    while(sscanf(&start[pos],"%d %n",&(vals[len]),&num)>0){len++;pos+=num;}
    uint64_t t1,t2;
    for(;blinks>0;blinks--){
        for(size_t j=len-1;j>=0;j--){
            if(!vals[j]) vals[j]+=1;
            else{
                t1=countDigits(vals[j]);
                if(t1&0x1) vals[j]*=2024;
                else{
                    t2=(vals[j]|0)
                }
            }
        }
    }

    return 0;
}