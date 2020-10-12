# indic language identification

Language identification tools are poor at supporting Indian languages, and worse at supporting Romanized variants.

This library addresses this particular use-case. The model is trained using weak labels obtained from an unsupervised
method [Palakodety, KhudaBukhsh & Carbonell, 2020].

The model is a `fasttext` model. 

## Install

* First install fasttext: `pip install fasttext`.
* Download the model: [link](https://storage.googleapis.com/indic-language-identification/fasttext_indic_merged_supervised_model_final.ftz)

## Predict

You can now use the model like you would any fasttext model:

`/path/to/fasttext predict fasttext_indic_merged_supervised_model_final.ftz -`


```
(base) ➜  indic_language_identification git:(master) ✗ ~/fastText/fasttext predict ~/aludra/pegasus/fasttext_indic_merged_supervised_model_final.ftz -
yeh kaun si bhasha hai
__label__hi_romanized
```

## Cite

If you use this work, do cite us:

```
```

(c) Onai 2020