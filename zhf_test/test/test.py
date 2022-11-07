if __name__ == "__main__":
    a = b = c = 1
    final_str = ""
    final_str += \
        f"""
{a}: {b} {{
    parameters:
        @display("i=device/satellite_vl");
    gates:
        ethg[{c}]; 
}}
"""
    print(final_str)
