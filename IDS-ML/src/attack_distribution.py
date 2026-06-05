import pandas as pd
import matplotlib.pyplot as plt

columns = [
    'duration','protocol_type','service','flag',
    'src_bytes','dst_bytes','land','wrong_fragment',
    'urgent','hot','num_failed_logins','logged_in',
    'num_compromised','root_shell','su_attempted',
    'num_root','num_file_creations','num_shells',
    'num_access_files','num_outbound_cmds',
    'is_host_login','is_guest_login','count',
    'srv_count','serror_rate','srv_serror_rate',
    'rerror_rate','srv_rerror_rate','same_srv_rate',
    'diff_srv_rate','srv_diff_host_rate',
    'dst_host_count','dst_host_srv_count',
    'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate',
    'dst_host_srv_serror_rate',
    'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate',
    'label',
    'difficulty'
]

data = pd.read_csv(
    "../dataset/KDDTrain+.txt",
    names=columns
)

top_attacks = data["label"].value_counts().head(10)

plt.figure(figsize=(10,6))
top_attacks.plot(kind="bar")

plt.title("Top 10 Attack Types")
plt.xlabel("Attack Type")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("../screenshots/attack_distribution.png")

plt.show()
