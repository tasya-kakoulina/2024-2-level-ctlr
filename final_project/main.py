"""
Final project implementation.
"""

# pylint: disable=unused-import
from pathlib import Path
from core_utils.constants import PROJECT_ROOT
from lab_6_pipeline.pipeline import UDPipeAnalyzer
from collections import defaultdict


def main() -> None:
    """
    Generate conllu file for provided corpus of texts.
    """
    path = PROJECT_ROOT / 'final_project'
    assets_path = path / 'assets' / 'pasternak'
    dist_path = path / 'dist'
    if not dist_path.exists():
        dist_path.mkdir(parents=True)
    text = ''
    for file in sorted(assets_path.iterdir()):
        if file.suffix == '.txt':
            with open(file, 'r', encoding='utf-8') as f:
                text += f.read()
                text += '\n'
    analyzer = UDPipeAnalyzer()
    analyzed = analyzer.analyze([text])

    with open(dist_path / 'auto_annotated.conllu', 'w', encoding='utf-8') as file:
        file.write(analyzed[0])



if __name__ == "__main__":
    main()
