
file_path = r'c:\myVSCode\PS6\PS6\templates\ownerApp\property_list.html'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace("request.GET.filter=='price_asc'", "request.GET.filter == 'price_asc'")
    new_content = new_content.replace("request.GET.filter=='price_desc'", "request.GET.filter == 'price_desc'")

    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated the file.")
    else:
        print("No changes needed or target string not found.")

except Exception as e:
    print(f"An error occurred: {e}")
