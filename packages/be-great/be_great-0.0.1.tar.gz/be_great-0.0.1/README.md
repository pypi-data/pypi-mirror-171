
[//]: # (![Screenshot]&#40;./imgs/GReaT_logo.png&#41;)
<p align="center">
<img src="./imgs/GReaT_logo.png" width="326"/>
</p>

<p align="center">
<strong>Generation of Realistic Tabular data</strong>
<br> with pretrained Transformer-based language models
</p>

&nbsp;
&nbsp;
&nbsp;

Our GReaT framework utilizes the capabilities of pretrained large language Transformer models to synthesize realistic tabular data. 
New samples are generated with just a few lines of code, following an easy-to-use API.

## GReaT Installation

The GReaT framework can be easily installed using with [pip](https://pypi.org/project/pip/): 
```bash
pip install be-great
```



## GReaT Quickstart

In the example below, we show how the GReaT approach is used to generate synthetic tabular data for the California Housing dataset.
```python
from be_great import GReaT
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True).frame

model = GReaT(llm='distilgpt2', epochs=50)
model.fit(data)
synthetic_data = model.sample(n_samples=100)
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kathrinse/be_great/blob/main/examples/Example_California_Housing.ipynb)

## GReaT Citation 
If you use GReaT, please link or cite our work:
```tex
@article{
}
```

## GReaT Acknowledgements

We sincerely thank the [HuggingFace](https://huggingface.co/) :hugs: framework. 
