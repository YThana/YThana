# Profile card generator

Regenerate `../profile.svg`:

1. (optional) Remove background from a new photo (macOS Vision):
   `swift liftsubject.swift ~/path/photo.jpeg subject.png`
2. Convert to ASCII art:
   `python3 ascii.py subject.png 96 > portrait.txt` (3rd arg = gamma, default 0.60)
3. Edit the `info` list in `gen_svg.py` (role, stack, projects, links), then:
   `python3 gen_svg.py portrait.txt ../profile.svg`
