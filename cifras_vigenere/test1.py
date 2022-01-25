from string import ascii_uppercase
from operator import itemgetter

xrange = range


def vigenere_decrypt(target_freqs, input):
    nchars = len (ascii_uppercase)
    ordA = ord ('A')
    sorted_targets = sorted (target_freqs)

    def frequency(input):
        result = [[c, 0.0] for c in ascii_uppercase]
        for c in input:
            result[c - ordA][1] += 1
        return result

    def correlation(input):
        result = 0.0
        freq = frequency (input)
        freq.sort (key=itemgetter (1))

        for i, f in enumerate (freq):
            result += f[1] * sorted_targets[i]
        return result

    cleaned = [ord (c) for c in input.upper () if c.isupper ()]
    best_len = 0
    best_corr = -100.0

    # Assume that if there are less than 20 characters
    # per column, the key's too long to guess
    for i in xrange (2, len (cleaned) // 20):
        pieces = [[] for _ in xrange (i)]
        for j, c in enumerate (cleaned):
            pieces[j % i].append (c)

        # The correlation seems to increase for smaller
        # pieces/longer keys, so weigh against them a little
        corr = -0.5 * i + sum (correlation (p) for p in pieces)

        if corr > best_corr:
            best_len = i
            best_corr = corr

    if best_len == 0:
        return ("Text is too short to analyze", "")

    pieces = [[] for _ in xrange (best_len)]
    for i, c in enumerate (cleaned):
        pieces[i % best_len].append (c)

    freqs = [frequency (p) for p in pieces]

    key = ""
    for fr in freqs:
        fr.sort (key=itemgetter (1), reverse=True)

        m = 0
        max_corr = 0.0
        for j in xrange (nchars):
            corr = 0.0
            c = ordA + j
            for frc in fr:
                d = (ord (frc[0]) - c + nchars) % nchars
                corr += frc[1] * target_freqs[d]

            if corr > max_corr:
                m = j
                max_corr = corr

        key += chr (m + ordA)

    r = (chr ((c - ord (key[i % best_len]) + nchars) % nchars + ordA)
         for i, c in enumerate (cleaned))
    return (key, "".join (r))


def main():
    encoded = """
       atmejaoheh arbwmaumsc qqcwoyhjqdy pwvypintnd eutidadrba namghegssq
       mxgizonwny etzidagmlq nbgmqmhicud iioqoxsmte ignqmksban bmxanjwrab
       mexqmvmndg zshpeuemat mewamzsmatm ezumpqoamw wrfixspgev gjadzwddrm
       hudtdhnbol whpozrsdeb shfokvnhazs nadjqtzdwg hupmirqnbw ifehtnqsbw
       gfuysnqqca fnrdscmvqv upekimpemkm qnxmzxmmfn qdzwsqbmem gpmilaeymy
       ysjyaqrkgg mczvsaaymu ztdhzpelwpm gvvngalwye pzvzcumkyp eqiodnikwa
       inerzokgld eiymoawjce cjennuauudp jvdxaavype avnztijmqc jqncumfibo
       mutqsiboet vqdpilsxat zqoadiboetv rzfuzwtmdv wbaiasm
       """

    portuguese_frequences = [
        0.1463, 0.0104, 0.0388, 0.0499, 0.1257, 0.0102, 0.0130,
        0.0078, 0.0619, 0.0040, 0.0002, 0.0278, 0.0474, 0.0445,
        0.0974, 0.0252, 0.0120, 0.0653, 0.0681, 0.0434, 0.0364,
        0.0158, 0.0004, 0.0025, 0.0001, 0.0047]

    (key, decoded) = vigenere_decrypt (portuguese_frequences, encoded)
    print ("Key:", key)
    print ("\nText:", decoded)


main ()