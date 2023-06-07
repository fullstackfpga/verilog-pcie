action = "simulation"
sim_tool = "iverilog_cocotb"
sim_top = "dma_if_axi"

iverilog_opt = "-g2012"
vvp_opt = "-fst"

iverilog_elab_param = {
    "defparam" : {"AXI_DATA_WIDTH"  : 64,
                  "AXI_ADDR_WIDTH" : 16,
                  "AXI_STRB_WIDTH" : 8,
                  "AXI_ID_WIDTH"   : 8,
                  "RAM_SEL_WIDTH"  : 2,
                  "RAM_ADDR_WIDTH" : 16,
                  "RAM_SEG_COUNT"  : 2,
                  "RAM_SEG_DATA_WIDTH" : 64,
                  "RAM_SEG_BE_WIDTH" : 8,
                  "RAM_SEG_ADDR_WIDTH" : 12,
                  "IMM_ENABLE" : 1,
                  "IMM_WIDTH" : 64,
                  "LEN_WIDTH" : 16,
                  "TAG_WIDTH" : 8,
                  "READ_OP_TABLE_SIZE" : 256,
                  "WRITE_OP_TABLE_SIZE" : 256,
                  "READ_USE_AXI_ID" : 0,
                  "WRITE_USE_AXI_ID" : 1,
                   }
}

files = [
    "../../rtl/dma_if_axi_rd.v",
    "../../rtl/dma_if_axi_wr.v",
    "../../rtl/dma_if_axi.v"
]

