from math import pi


def main():
    input_string = """
#1 Picnic	6.83	10.16	$0.28
#1 Tall	7.78	11.91	$0.43
#2	8.73	11.59	$0.45
#2.5	10.32	11.91	$0.61
#3 Cylinder	10.79	17.78	$0.86
#5	13.02	14.29	$0.83
#6Z	5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10	15.72	17.78	$1.53
#211	6.83	12.38	$0.34
#300	7.62	11.27	$0.38
#303	8.10	11.11	$0.42
    """.strip()

    split_by_lines = input_string.split("\n")
    split_by_tabs = []

    for line in split_by_lines:
        split_by_tabs.append(line.split("\t"))

    for can_specs in split_by_tabs:
        radius = float(can_specs[1])
        height = float(can_specs[2])

        can_specs.append(compute_storage_efficiency(radius, height))

    split_by_tabs.sort(key= lambda x: x[4], reverse=True)

    for i, can_specs in enumerate(split_by_tabs):
        print(f"{i + 1}. Name:{can_specs[0]}\n{'':{len(str(i + 1)) + 2}}Efficiency: {can_specs[4]:.2f}\n")
    

def compute_volume(radius, height):
    volume = pi * radius ** 2 * height
    return volume
                                                                                            
def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area
  
def compute_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area


main()