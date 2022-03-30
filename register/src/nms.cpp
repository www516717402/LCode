#include <torch/types.h>
#include "pytorch_device_register.hpp"

int CPU = 0, GPU=1, NPU=2;

double nms_cpu(int boxes, int scores, float iou_threshold, int offset) {
  return 0;
}

double nms_impl(int boxes, int scores, float iou_threshold, int offset);


REGISTER_DEVICE_IMPL(nms_impl, CPU, nms_cpu);

double nms_gpu(int boxes, int scores, float iou_threshold, int offset) {
  return 10;
}

REGISTER_DEVICE_IMPL(nms_impl, GPU, nms_gpu);

double nms_npu(int boxes, int scores, float iou_threshold, int offset) {
  return 20;
}

REGISTER_DEVICE_IMPL(nms_impl, NPU, nms_npu);

int kkk = DISPATCH_DEVICE_IMPL(nms_impl, 1, 1, 1, 1);

double softnms_cpu(int boxes, int scores, float iou_threshold, int offset) {
  return 30;
}

double softnms_cpu_impl(int boxes, int scores, float iou_threshold, int offset);

REGISTER_DEVICE_IMPL(softnms_cpu_impl, CPU, softnms_cpu);



