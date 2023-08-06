
#ifndef K2_MODELIMP_H
#define K2_MODELIMP_H

#include <Model.h>
#include <stdint.h>
#include <string>

#include "../FeatureExtract.h"
#include "../Tensor.h"
#include "../Vocab.h"
#include "Decoder.h"
#include "Encoder.h"
#include "Joiner.h"
#include "ModelParams.h"
#include "PositionEncoding.h"

using namespace kaldi2;

namespace kaldi2 {

class ModelImp : public Model {
  private:
    FeatureExtract *fe;
    kaldi2::ModelParamsHelper *p_helper;

    PositionEncoding *pos_enc;
    Encoder *encoder;
    Joiner *joiner;
    Decoder *decoder;
    Vocab *vocab;

  public:
    ModelImp(const char *path, int mode);
    ~ModelImp();
    void reset();
    string forward_chunk(float *din, int len, int flag);
    string forward(float *din, int len, int flag);
    string rescoring();

    string greedy_search(Tensor<float> *&encoder_out);
};

} // namespace kaldi2
#endif
