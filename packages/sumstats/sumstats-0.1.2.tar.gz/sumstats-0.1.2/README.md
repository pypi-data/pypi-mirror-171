# sumstats

Utilities for working with GWAS summary statistics

This is a package on pypi so you can get it with `pip install sumstats`

## Fine mapping

If inputs are p-values, minor allele frequency, and sample size, first calculate natural log bayes factors and then calculate the PPA's.

To set things up:

```python
import math
import sumstats
N = <sample size>
p_values = <p_values of variants in fine-mapping region>
mafs = <minor allele frequencies of variants in fine-mapping region>
```

To calculate natural log bayes factors or "lnbf":

```python
lnbfs = [sumstats.approx_lnbf(pval=p, freq=maf, sample_size=N) for p, maf in zip(p_values, mafs)]
```

To caluclate posterior probability of association:
```python
normalizing_coefficient = sumstats.log_sum(lnbfs)
ppa = [math.exp(lnbf - normalizing_coefficient) for lnbf in lnbfs]
```
