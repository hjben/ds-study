import torch, os

class SetGPU():
    def __init__(self):
        self.use_cuda = False
        self.ngpus = 0
        self.gpu_list = list()   

    def find_gpu(self):
        if torch.cuda.is_available():
            self.use_cuda = True
            self.ngpus = torch.cuda.device_count()
            self.gpu_list = [torch.device(f'cuda:{i}') for i in range(self.ngpus)]
            print('Available GPU devices ==> ', self.ngpus)
        else:
            print('GPU not found')

    def set_gpu(self, device):
        if isinstance(device, int):
            device = str(device)

        if device=='cpu' or device=='-1':
            os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

        elif device in [str(i) for i in range(self.ngpus)]:
            os.environ['CUDA_VISIBLE_DEVICES'] = device

        else:
            raise ValueError(f'Not Supported Device==[{device}]')

if __name__=="__main__":
    set_gpu = SetGPU()
    set_gpu.find_gpu()
    print(set_gpu.gpu_list)

    r = torch.randn((2, 3), device=set_gpu.gpu_list[1])
    print(r.device)