# Color Palette

#000000
#1D2B53
#7E2553
#008751

#AB5236
#5F574F
#C2C3C7
#FFF1E8

#FF004D
#FFA300
#FFEC27
#00E436

#29ADFF
#83769C
#FF77A8
#FFCCAA

![Pico 8 Palette](./palette.png)

## Functional Requirements
1. Sprite Painting Tool, Sprite size 16x16 (w/ variable canvas size)
2. Exports a sprite sheet to .bmp
3. Provides imports for sprite painting tool and sprite loading API to end user
4. Ability to Hot reload sprite

## Non-Functional Requirements
1. Pygame Typing
2. No shit code (Oblique allowed)

## Design decisions
1. Transform the sprite painted to .bmp, transform the pixel info in .bmp to pygame Surface. (Memory to Memory drawing)
2. Provide a SPRITE interface which takes in sprite_id (as stored in .bmp), position, TILE_SIZE. 

# Future Scope (Extreme Obliqueness)
1. Provide rewire handlers to visit and import the Plugin API while importing pygame (Applying a plugin bind to object imports)