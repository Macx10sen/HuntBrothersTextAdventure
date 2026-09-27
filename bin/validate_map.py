import yaml
import sys
import os


def validate(map_path):
    with open(map_path, 'r') as f:
        map_data = yaml.load(f, Loader=yaml.SafeLoader)

    errors = []
    room_names = set(map_data.keys())

    for room_name, room_data in map_data.items():
        # Check required room fields
        if 'description' not in room_data:
            errors.append(f"[{room_name}] missing 'description'")
        if 'exits' not in room_data or not room_data['exits']:
            errors.append(f"[{room_name}] has no exits")
            continue

        for direction, exit_data in room_data['exits'].items():
            prefix = f"[{room_name}] exit '{direction}'"

            # Check required exit fields
            for field in ('destination', 'description', 'locked'):
                if field not in exit_data:
                    errors.append(f"{prefix} missing '{field}'")

            # Check destination exists
            destination = exit_data.get('destination')
            if destination and destination not in room_names:
                errors.append(f"{prefix} destination '{destination}' does not exist")

            # Check locked doors have a password
            if exit_data.get('locked') and 'password' not in exit_data:
                errors.append(f"{prefix} is locked but has no 'password'")

    return errors


if __name__ == '__main__':
    map_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join('bin', 'map_data', 'escapeRoom.yaml')

    print(f"Validating {map_path}...")
    errors = validate(map_path)

    if errors:
        print(f"Found {len(errors)} error(s):\n")
        for error in errors:
            print(f"  {error}")
        sys.exit(1)
    else:
        print("All good.")
