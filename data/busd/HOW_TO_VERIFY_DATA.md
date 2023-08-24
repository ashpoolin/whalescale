# How to Verify the Data's Chain of Custody

## Import GPG Key
gpg --import ashpoolin.gpg

## Verify Signature on SHASUMS.txt
gpg --verify SHASUMS.txt.sig 

## Confirm GPG signature fingerprint
See Fingerprint on my Twitter account [at solanobahn](https://twitter.com/solanobahn). Confirm it matches the detached, verified signature for the SHASUMS.txt file.

## Confirm SHA256 Checksums
shasum -a 256 -c SHASUMS.txt

These should all read OK:
busd_whalescale_labeled_top100.csv: OK
busd_indexes.zip: OK
receiver_id.txt: OK
sender_id.txt: OK
uiamount.txt: OK
busd_whalescale_labeled.zip: OK
P_t_final_links_only_indexed.csv: OK
busd_data_summary_indexed.zip: OK
busd_transaction_hashes.zip: OK