# Tensorflow Model Playground

- Different tensorflow Deep Learning model & Helper Function.
- Currently Included Generative Adversarial Networks and som ehelper function.

## Package File Structure
[![fs](https://ik.imagekit.io/43bd8tl1l5kl/tf-ml-pg/fs_5lnQW6vq7.png?ik-sdk-version=javascript-1.4.3&updatedAt=1665724957691 "fs")](https://ik.imagekit.io/43bd8tl1l5kl/tf-ml-pg/fs_5lnQW6vq7.png?ik-sdk-version=javascript-1.4.3&updatedAt=1665724957691 "fs")

## Usage Example
### Generative Adversarial Networks
* Simple CycleGAN

```python
from modelpg.GAN import build_generator , build_descriminator , composite_model,train_model
generator_1 = build_generator(image_shape=(256,256))
generator_2 = build_generator(image_shape=(256,256))

descriminator_1 = build_descriminator(image_shape=(256,256))
descriminator_2 = build_descriminator(image_shape=(256,256))

composite_1 = composite_model(generator_1,descriminator_1,generator_2,image_shape=(256,256))
composite_2 = composite_model(generator_2,descriminator_2,generator_1,image_shape=(256,256))

train_model(descriminator_1,descriminator_2,generator_1,generator_2,composite_1,composite_2,dataset,epochs=100)
```

- After training use each generator to generate images.