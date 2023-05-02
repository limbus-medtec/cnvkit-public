"""Hard-coded parameters for CNVkit. These should not change between runs."""
# Filter thresholds used in constructing the reference (log2 scale)
MIN_REF_COVERAGE = -5.0
MAX_REF_SPREAD = 1.0
NULL_LOG2_COVERAGE = -20.0

# Thresholds used in GC-content masking of bad bins at 'fix' step
GC_MIN_FRACTION = 0.3
GC_MAX_FRACTION = 0.7

# Fragment size for paired-end reads
INSERT_SIZE = 250

# Target/bin names that are not meaningful gene names
# (In some UCSF panels, "CGH" probes denote selected intergenic regions)
IGNORE_GENE_NAMES = ("-", ".", "CGH")
ANTITARGET_NAME = "Antitarget"
ANTITARGET_ALIASES = (ANTITARGET_NAME, "Background")

# PAR1/2 start/end definitions
PSEUDO_AUTSOMAL_REGIONS = {
    "grch37": [60001,  2699520, 154931044, 155260560],
    "grch38": [10001 , 2781479, 155701383, 156030895],
}
SUPPORTED_GENOMES_FOR_PAR_HANDLING = PSEUDO_AUTSOMAL_REGIONS.keys()