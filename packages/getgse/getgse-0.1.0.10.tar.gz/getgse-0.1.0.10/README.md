# Python package for retrieving metadata and downloading datasets from GEO

## CLI Usage
`getgse` supports CLI(command line interface) usage.
```bash
$ getgse --gse GSE81903
```

## Installation
To install using pip:
```bash
pip install getgse
```

> We do not support the anaconda package yet..

### Dependencies
```
pysradb>=1.4.2
docker
wget
```

## Using getgse
### Downloading multiple GSE project
`getgse` supports multiple arguments like below.
```bash
getgse --gse GSE148822 GSE159541 GSE159699 GSE161199 GSE164788 GSE173955 GSE174367 GSE184942 GSE136243
[GSE148822]
exploring SRP256885 in GSE148822
SRRs: ['SRR11560748', 'SRR11560747', 'SRR11560746', 'SRR11560745', 'SRR11560744', 'SRR11560743', 'SRR11560742', 'SRR11560741', 'SRR11560740', 'SRR11560739', 'SRR11560738', 'SRR11560737', 'SRR11560736', 'SRR11560735', 'SRR11560734', 'SRR11560733', 'SRR11560732', 'SRR11560731', 'SRR11560730', 'SRR11560729', 'SRR11560728', 'SRR11560727', 'SRR11560726', 'SRR11560725', 'SRR11560724', 'SRR11560723', 'SRR11560722', 'SRR11560721', 'SRR11560720', 'SRR11560719', 'SRR11560718', 'SRR11560717', 'SRR11560716', 'SRR11560715', 'SRR11560714', 'SRR11560713']
[GSE159541]
exploring SRP287832 in GSE159541
All files are downloaded.
[GSE159699]
exploring SRP287843 in GSE159699
All files are downloaded.
[GSE161199]
exploring SRP292025 in GSE161199
All files are downloaded.
[GSE164788]
exploring SRP301436 in GSE164788
Downloading GSE164788/SRR13418571.fastq.gz from http://ftp.sra.ebi.ac.uk/vol1/fastq/SRR134/071/SRR13418571/SRR13418571.fastq.gz
100% [■■■■■■■■■■■■■■■■■■■■■■■■■■■■]
...
```