action = "simulation"
sim_tool = "iverilog"
sim_top = "dma_if_axi"

#sim_post_cmd = "vsim -do ../vsim.do -c camera_tb"

files = [
    "../../rtl/dma_if_axi_rd.v",
    "../../rtl/dma_if_axi_wr.v",
    "../../rtl/dma_if_axi.v"
]

#modules = {
#  "local" : [ "../../rtl" ],
#}
