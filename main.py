import re
import os

import textract


class ThesisFinder:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.decoded_content = self.process_file(file_name)

    @staticmethod
    def process_file(file_name: str):
        base_dir = os.getcwd()
        text = textract.process(f'{base_dir}/{file_name}')
        text = text.decode()
        return text

    def find_list_of_matches(self, pattern: str):
        new_pattern = pattern + r'(.*[\n]*[\t]*)'
        matches = re.findall(new_pattern, self.decoded_content)
        matches = [re.sub(pattern, "", match) for match in matches]
        return matches

    def find_matches_before_pattern(self, pattern: str) -> str:
        new_pattern = r'.*' + pattern
        matches = re.findall(new_pattern, self.decoded_content)
        matches = [re.sub(pattern, "", match) for match in matches]
        if not len(matches):
            return "not found"
        return matches[0]

    def find_matches_after_pattern(self, pattern: str) -> str:
        new_pattern = pattern + r'.*'
        matches = re.findall(new_pattern, self.decoded_content)
        matches = [re.sub(pattern, "", match) for match in matches]
        if not len(matches):
            return "not found"
        return matches[0]

    @staticmethod
    def add_extra_space_to_patterns(patterns: list, index: str = "after") -> str:
        extra_space = '[\n]*[\s]*'
        joined_pattern = ''
        for pattern in patterns:
            if index == "before":
                joined_pattern = extra_space + pattern
            else:
                joined_pattern = pattern + extra_space

        return joined_pattern

    def get_student_name(self):
        pattern = self.add_extra_space_to_patterns([r'دانشجو:'])
        name_matches = self.find_matches_after_pattern(pattern)
        return name_matches

    def get_guide_name(self):
        pattern = self.add_extra_space_to_patterns([r'استاد راهنما:'])
        name_matches = self.find_matches_after_pattern(pattern)
        return name_matches

    def get_advisor_name(self):
        pattern = self.add_extra_space_to_patterns([r'استاد مشاور:'])
        name_matches = self.find_matches_after_pattern(pattern)
        return name_matches

    def get_thesis_title(self):
        pattern = self.add_extra_space_to_patterns([r'استاد راهنما:'], "before")
        name_matches = self.find_matches_before_pattern(pattern)
        return name_matches

    def get_study_field(self):
        pattern = self.add_extra_space_to_patterns([r'گروه'])
        name_matches = self.find_matches_after_pattern(pattern)
        return name_matches

    def get_college_name(self):
        pattern = self.add_extra_space_to_patterns([r'دانشکده'])
        name_matches = self.find_matches_after_pattern(pattern)
        return name_matches

    def get_persian_summary(self):
        pattern = self.add_extra_space_to_patterns([r'چکیده'])
        name_matches = self.find_matches_after_pattern(pattern)
        return name_matches

    def get_english_summary(self):
        pattern = self.add_extra_space_to_patterns([r'Abstract'])
        name_matches = self.find_matches_after_pattern(pattern)
        return name_matches

    def get_references_list(self):
        pattern = self.add_extra_space_to_patterns([r'منابع و مآخذ'])
        name_matches = self.find_list_of_matches(pattern)
        return name_matches

    def start_search(self):
        print(self.get_student_name(), "\n")
        print(self.get_guide_name(), "\n")
        print(self.get_advisor_name(), "\n")
        print(self.get_thesis_title(), "\n")
        print(self.get_study_field(), "\n")
        print(self.get_college_name(), "\n")
        print(self.get_persian_summary(), "\n")
        print(self.get_english_summary(), "\n")
        print(self.get_references_list(), "\n")


if __name__ == "__main__":
    thesis_finder = ThesisFinder("پایان نامه شادی پورقدیری.docx")
    thesis_finder.start_search()
