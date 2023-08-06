import logging as l
import typing as t
import zipfile as zf


def split_comma_separated_list(list_string: str) -> list:
    items: list = list_string.split(',')

    if '' in items:
        l.warning(f'Blank items detected in the comma separated list: "{list_string}". Removing blanks...')
        items = [item for item in items if item != '']

    # If the items end up being an empty list
    if not items:
        raise RuntimeError(f'ERROR - BAD INPUT: Empty list provided: "{list_string}"')

    return items


def get_molecular_attribute_args(args: dict) -> tuple:
    formula: str = args['--formula']
    exact_mass: list = args['--exact-mass']
    molecular_weight: list = args['--molecular-weight']

    # exact_mass and molecular_weight will be [] (empty list) if not specified in the commandline args
    if exact_mass:
        exact_mass: t.Union[float, tuple] = _get_range_values(range_values=exact_mass, value_type=float)
    else:
        exact_mass = None

    if molecular_weight:
        molecular_weight: t.Union[int, tuple] = _get_range_values(range_values=molecular_weight, value_type=int)
    else:
        molecular_weight = None

    return formula, exact_mass, molecular_weight


def _get_range_values(range_values: t.Union[int, float, tuple], value_type: type) -> t.Union[int, float, tuple]:
    if len(range_values) == 1:
        [val] = range_values

        return value_type(val)
    elif len(range_values) == 2:
        [min_val, max_val] = range_values

        return value_type(min_val), value_type(max_val)
    else:
        raise ValueError(
            f'Range can only be specified by two values but {len(range_values)} values were provided: '
            f'{", ".join(str(range_value) for range_value in range_values)}'
        )


def save_to_zip_archive(zip_archive_path: str, zip_file_name: str, file_content: t.Union[str, bytes]) -> None:
    if zip_file_name is None:
        # Set the file name to the same name as the zip archive minus the .zip extension.
        zip_file_name = zip_archive_path[:-len('.zip')]

    with zf.ZipFile(zip_archive_path, 'a') as zip_file:
        zip_file.writestr(zip_file_name, file_content)


class staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()
