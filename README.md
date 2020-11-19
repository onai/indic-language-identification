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
(base) ➜  indic_language_identification git:(master) ✗ ~/fastText/fasttext predict /path/to/fasttext_indic_merged_supervised_model_final.ftz -
yeh kaun si bhasha hai
__label__hi_romanized
```

## Cite

If you use this work, do cite us:

```
@inproceedings{palakodety-khudabukhsh-2020-annotation,
    title = "Annotation Efficient Language Identification from Weak Labels",
    author = "Palakodety, Shriphani  and
      KhudaBukhsh, Ashiqur",
    booktitle = "Proceedings of the Sixth Workshop on Noisy User-generated Text (W-NUT 2020)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.wnut-1.24",
    pages = "181--192",
}
```

(c) Onai 2020
