# bnNumerizer
Bangla number to Bangla string converter based on the work [banglakit/number-to-bengali-word](https://github.com/banglakit/number-to-bengali-word)

```
original authors: aniruddha-adhikary,Mahir Labib Chowdhury
pypi: mnansary
```

# install
```python
pip install bnnumerizer
```
# useage
```python
from bnnumerizer import numerize
text= "বিল গেটসের ব্যাংক ব্যালেন্স ২২২১২৩৪৫৬.১২৩৪ টাকা। এর মধ্যে আমার অর্থের পরিমাণ ৩৪৫ টাকা মাত্র "
numerize(text)
```
```
'বিল গেটসের ব্যাংক ব্যালেন্স বাইশ কোটি একুশ লক্ষ তেইশ হাজার চার শত ছাপ্পান্ন দশমিক এক দুই তিন চার টাকা। এর মধ্যে আমার অর্থের পরিমাণ তিন শত পঁয়তাল্লিশ টাকা মাত্র '
```
# Limitations
* can not convert numbers > "৯৯৯৯৯৯৯৯৯" 

# Citing
* if you find the word use full please star/ cite the **Orininal Repository**: https://github.com/banglakit/number-to-bengali-word
