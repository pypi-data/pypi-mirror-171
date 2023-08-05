# Pulse-Coupled-Neural-Network
A simple python implementation for Pulse Coupled Neural Networks (PCNN)


## Instructions

1. Install:

```
pip install pulse-coupled-neural-networks
```

2. Example:

```python
import matplotlib.pyplot as plt
import numpy as np
from pulse-coupled-neural-networks import ClassicalPCNN

image = np.array([
		[230, 230, 230, 230, 115, 115, 115, 115],
        [230, 230, 230, 230, 115, 115, 115, 115],
        [230, 230, 205, 205, 103, 103, 115, 115],
        [230, 230, 205, 205, 103, 103, 115, 115],
        [230, 230, 205, 205, 103, 103, 115, 115],
        [230, 230, 230, 230, 115, 115, 115, 115],
        [230, 230, 230, 230, 115, 115, 115, 115]
	])

model = ClassicalPCNN(image.shape, kernel)
segm_image = model.segment_image(image, gamma, beta, v_theta, kernel_type='gaussian')

plt.imshow(image)
plt.imshow(segm_image)
plt.show()
```

3. Ride the space skyway home to 80s Miami