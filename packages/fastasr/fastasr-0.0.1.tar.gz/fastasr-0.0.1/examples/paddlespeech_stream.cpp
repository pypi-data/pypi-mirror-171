#include <iostream>
#ifndef _WIN32
#include <sys/time.h> // for gettimeofday()
#else
#include <win_func.h>
#endif
#include "Audio.h"
#include "Model.h"

using namespace std;

int main(int argc, char *argv[])
{
    struct timeval start, end;
    int len = 1360;
    Audio audio(len);

    gettimeofday(&start, NULL);
    Model *mm = create_model(argv[1], 1);
    mm->reset();
    gettimeofday(&end, NULL);
    long seconds = (end.tv_sec - start.tv_sec);
    long micros = ((seconds * 1000000) + end.tv_usec) - (start.tv_usec);
    printf("Model initialization takes %lfs.\n", (double)micros / 1000000);

    float *buff;
    int sum = 0;
    audio.loadwav(argv[2]);
    audio.disp();

    int flag = S_MIDDLE;

    gettimeofday(&start, NULL);
    while (flag == S_MIDDLE) {
        flag = audio.fetch_chunck(buff, len);
        sum += len;
        string msg = mm->forward_chunk(buff, len, flag);
        cout << "Current Result: \"" << msg << "\"." << endl;
    }
    string msg = mm->rescoring();
    gettimeofday(&end, NULL);
    cout << "Final Result: \"" << msg << "\"." << endl;

    seconds = (end.tv_sec - start.tv_sec);
    micros = ((seconds * 1000000) + end.tv_usec) - (start.tv_usec);
    printf("Model inference takes %lfs.\n", (double)micros / 1000000);
}
