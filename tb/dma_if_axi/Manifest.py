action = "simulation"
sim_tool = "iverilog"
sim_top = "dma_if_axi"

iverilog_opt = "-fst"
vvp_opt = "-test"

#sim_post_cmd = "vsim -do ../vsim.do -c camera_tb"

iverilog_elab_param = {
    "defparam" : {"AXI_DATA_WIDTH" : 64,
                   "AXI_ADDR_WIDTH" : 16,
                   "AXI_STRB_WIDTH" : """AXI_DATA_WIDTH/8""",
                   "AXI_ID_WIDTH" : 8,
                   "RAM_SEL_WIDTH" : 2,
                   "RAM_ADDR_WIDTH" : 16,
                   "RAM_SEG_COUNT" : 2,
                   }
}

files = [
    "../../rtl/dma_if_axi_rd.v",
    "../../rtl/dma_if_axi_wr.v",
    "../../rtl/dma_if_axi.v"
]

#modules = {
#  "local" : [ "../../rtl" ],
#}
