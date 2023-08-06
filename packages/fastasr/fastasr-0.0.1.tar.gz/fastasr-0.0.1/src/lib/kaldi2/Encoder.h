
#ifndef K2_ENCODER_H
#define K2_ENCODER_H

#include <stdint.h>

#include "../Tensor.h"
#include "EmbedLayer.h"
#include "ModelParams.h"
#include "PositionEncoding.h"
#include "SubEncoder.h"

using namespace kaldi2;

namespace kaldi2 {
class Encoder {
  private:
    int cache_size;
    EncoderParams *params;
    EmbedLayer *embed;
    PositionEncoding *pos_enc;
    SubEncoder *subencoder[12];
    // LayerNorm *after_norm;

  public:
    Encoder(EncoderParams *params, PositionEncoding *pos_enc, int mode);
    ~Encoder();
    void reset();
    void forward(Tensor<float> *&din);
};
} // namespace kaldi2

#endif
