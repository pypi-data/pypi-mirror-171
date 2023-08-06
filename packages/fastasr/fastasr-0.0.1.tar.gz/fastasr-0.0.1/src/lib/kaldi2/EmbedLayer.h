
#ifndef K2_EMBEDLAYER_H
#define K2_EMBEDLAYER_H

#include <stdint.h>

#include "../Tensor.h"
#include "ModelParams.h"

using namespace kaldi2;
namespace kaldi2 {

class EmbedLayer {
  private:
    EncEmbedParams *params;
    void get_conv_ind(int in_row, int in_column, int kernel, int stride,
                      int padding, int &out_row, int &out_column,
                      int *&out_idxs);
    void conv0_forward(Tensor<float> *&din);
    void conv1_forward(Tensor<float> *&din);
    void conv2_forward(Tensor<float> *&din);
    void linear_out_forward(Tensor<float> *&din);
    void norm_forward(Tensor<float> *&din);

  public:
    EmbedLayer(EncEmbedParams *params);
    ~EmbedLayer();
    void forward(Tensor<float> *&din);
};

} // namespace kaldi2

#endif
