# app.py
import streamlit as st
import time

# Set up page
st.set_page_config(
    page_title="CPU Instruction Visualizer",
    layout="centered"
)

st.title("🧠 Basic CPU Instruction Visualizer")
st.caption("Demonstration of fundamental CPU operations for AMD internship")

# Instruction set
INSTRUCTIONS = {
    "ADD": "Add two registers",
    "MOV": "Move value between registers",
    "CMP": "Compare two values",
    "JMP": "Jump to memory address",
    "LOAD": "Load from memory",
    "STORE": "Store to memory"
}

# CPU state
registers = {"AX": 0, "BX": 0, "CX": 0, "DX": 0}
memory = {"0x1000": 0, "0x1004": 0, "0x1008": 0}
program_counter = 0

# UI components
st.sidebar.header("CPU Simulator")
selected_instruction = st.sidebar.selectbox(
    "Select Instruction", 
    list(INSTRUCTIONS.keys())
)

desc = st.sidebar.markdown(f"**Description:** {INSTRUCTIONS[selected_instruction]}")

# Display CPU state
st.header("CPU State")
reg_cols = st.columns(4)
for i, (reg, val) in enumerate(registers.items()):
    with reg_cols[i]:
        st.metric(label=reg, value=val)

st.subheader("Memory")
mem_cols = st.columns(3)
for i, (addr, val) in enumerate(memory.items()):
    with mem_cols[i]:
        st.text_input(label=addr, value=val, disabled=True)

# Visualize instruction execution
def visualize_instruction(instruction):
    global program_counter
    status = st.empty()
    assembly = st.empty()
    
    # Show assembly code
    assembly.code(f"{program_counter}: {instruction}", language="asm")
    
    # Animation sequence
    status.info("🔄 Fetching instruction from memory...")
    time.sleep(1)
    
    status.info("🔍 Decoding instruction...")
    time.sleep(0.5)
    
    status.info("⚡ Executing operation...")
    time.sleep(1)
    
    # Update state based on instruction
    if instruction == "ADD":
        registers["AX"] += registers["BX"]
        status.success("✅ AX = AX + BX")
    elif instruction == "MOV":
        registers["CX"] = registers["AX"]
        status.success("✅ CX = AX")
    elif instruction == "LOAD":
        memory["0x1000"] = registers["AX"]
        status.success("✅ [0x1000] = AX")
    
    program_counter += 1

# Execute button
if st.button(f"Execute {selected_instruction}"):
    visualize_instruction(selected_instruction)

# Explanation section
st.header("How CPUs Process Instructions")
st.markdown("""
1. **Fetch**: Retrieve instruction from memory
2. **Decode**: Determine what operation to perform
3. **Execute**: Carry out the operation
4. **Writeback**: Update registers/memory

This simplified visualization shows the core workflow of AMD processors like Ryzen and EPYC.
""")

# Footer
st.markdown("---")
st.caption("Project for AMD Software Internship Application | Demonstrates CPU fundamentals")
