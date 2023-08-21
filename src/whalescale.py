import torch                                                                                                                                                                                                                                                                                                                                                                                                                                                        
import numpy as np   

source = np.loadtxt("./from_id.csv", dtype=int)
destination = np.loadtxt("./to_id.csv", dtype=int)
data = np.loadtxt("./data.csv", dtype=float)
print("")
print(f"source: {source}")
print(f"destination: {destination}")
print(f"data: {data}")
print("")
rows = source.size
cols = destination.size
print(f"rows: {rows}")
print(f"cols: {cols}")
ind = torch.tensor(np.array([source,destination]))
print(f"ind: {ind}")

print("")
A = torch.sparse_coo_tensor(indices = ind, values = torch.tensor(data), size=[rows,cols])
print(f"sparse: {A}")
print("")
#D = A.to_dense()
#print(f"dense: {D}") 

print(f"data: {data}")
data = np.ones(data.size)
data_reshaped = data.reshape(1, -1)
data_nx1 = np.transpose(data_reshaped)
P_0 = torch.tensor(data_nx1)

A_normalized = A / torch.norm(A)
A_transposed = torch.t(A_normalized)
print(f"A^T: {A_transposed}")

# NOW WRITE THE REDACTED ALGORITHM
# LOOP
residual = 1000000000
threshold = 0.001
iteration = 1
while residual > threshold:
  P_t = A_transposed.mm(P_0)
  difference = P_t - P_0
  residual = torch.norm(difference)
  print(f"residual: {residual}")
  P_0 = P_t
  iteration += 1

if residual < threshold:
  print(f"result converged to residual < {residual} in {iteration} iterations.")
else:
  print(f"failed to converge.")

print(f"final P_t: {P_t}")

# Convert the tensor to a NumPy array                                                                                                                                                                                                                                                                
numpy_array = P_t.numpy()                                                                                                                                                                                                                                                                         
# Save the NumPy array to a CSV file                                                                                                                                                                                                                                                                 
np.savetxt('P_t_final_links_only.csv', numpy_array, delimiter=',') 
