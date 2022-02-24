
import sys
import json
import json_delta


if len(sys.argv) < 2:
    print("Missing argument name of the JSON override file")
    exit(1)

override_file = sys.argv[1]

# no version specified
version = "all"
if len(sys.argv) >= 3:
    version = sys.argv[2]

fetched_api_path = f"pingaccesssdk/source/apis/{override_file}"

override_path = f"src/overrides/{version}/{override_file}"
delta_dest_path = f"src/overrides/{version}/{override_file.split('.')[0]}.delta"

api_dict = json.loads(open(fetched_api_path).read())
override_dict = json.loads(open(override_path).read())

delta_dict = json_delta.diff(api_dict, override_dict)

if not delta_dict:
    print("No difference detected between files, skipping save...")
    exit(0)

with open(delta_dest_path, "w+") as file_handle:
    file_handle.write(json.dumps(delta_dict))
    print(f"Saved override delta file in {delta_dest_path}...")
