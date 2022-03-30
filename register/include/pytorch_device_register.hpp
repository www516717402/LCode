
#ifndef PYTORCH_DEVICE_REGISTRY_H
#define PYTORCH_DEVICE_REGISTRY_H
#include <cassert>
#include <functional>
#include <map>
#include <type_traits>
// Registry
// template <typename F>
// class DeviceRegistry;
// 
// template <typename Ret, typename... Args>
template <typename F>
class DeviceRegistry {
 public:
  using FunctionType = F;
  static const int MAX_DEVICE_TYPES = 3;

  // device range 0 or 1
  void Register(int device, FunctionType function) {
    funcs_[device] = function;
  }

  FunctionType Find(int device) const {
    return funcs_[device];
  }

  static DeviceRegistry& instance() {
    static DeviceRegistry inst;
    return inst;
  }

 private:
  DeviceRegistry() {
    for (int i = 0; i < MAX_DEVICE_TYPES; ++i) {
      funcs_[i] = nullptr;
    }
  };
  FunctionType funcs_[MAX_DEVICE_TYPES];
};

template <typename R, typename... Args>
auto Dispatch(const R& registry, const char* name, Args&&... args) {
  auto f_ptr = registry.Find(2);
  return f_ptr(std::forward<Args>(args)...);
}

#define DEVICE_REGISTRY(key) DeviceRegistry<decltype(&(key))>::instance()

#define REGISTER_DEVICE_IMPL(key, device, value)           \
  struct key##_##device##_registerer {                     \
    key##_##device##_registerer() {                        \
      DEVICE_REGISTRY(key).Register(device, value); \
    }                                                      \
  };                                                       \
  key##_##device##_registerer _##key##_##device##_registerer;

#define DISPATCH_DEVICE_IMPL(key, ...) \
  Dispatch(DEVICE_REGISTRY(key), #key, __VA_ARGS__)

#endif  // PYTORCH_DEVICE_REGISTRY

