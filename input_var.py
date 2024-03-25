##Cluster reset
Cluster_reset ="no"
platform_path="/home/labadmin/TRILLIUM_CNF_PLATFORM_4.0.3/platform"
enable_dual_stack_networks="No"
# If the test bed is capacity
capacity= "no"

# Copy the build from remote server
new_upgrade = "yes"
remote_host_ip = "yamuna"
remote_path = "/home/pchinnap/5.1.0_EA3"
remote_username = "sobirada"
remote_password = "01Password!"

## Node IP
cluster_ip = "172.27.28.110"

# The image version want to uninstall (N build)
old_image_version = "5.1.0"

# The image version want to install (N+1)
new_image_version = "5.1.0"

# N2 IP address for gNB and AMF connection
n2_ip ="11.2.2.100"

# NEF IP address, for the release above 4.2.0
nef = "yes"
nef_ee ="172.27.28.110"
nef_pp ="172.27.28.110"

ingress_ip ="172.27.29.88"
# DN interface PCI
n6_pci = "0000:00:0a.0"

# Ngu interface PCI
n3_pci = "0000:00:09.0"

# Build path of the upgrade build (N+1)
path = "/home/labadmin/5GC_5.1.0_EA3"

# Build path of the N build
old_buildpath ="/home/labadmin/5GC_5.1.0_EA3"

# If Yes data will be cleared from mnt direcotry
Clear_data_from_mnt_folders = "Yes"

# if testbed is baremetal please sriov as yes
sriov = "no"
