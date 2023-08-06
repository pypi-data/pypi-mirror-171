"""Handler for editting outbreaks"""
from typing import Any

from ... import user_input_handler, helper
from . import main_story

def get_available_chapters(outbreaks: dict[int, Any]) -> list[str]:
    """Get available chapters"""

    available_chapters: list[str] = []
    for chapter in outbreaks:
        index = chapter
        if index > 2:
            index -= 1
        available_chapters.append(main_story.CHAPTERS[index])
    return available_chapters


def set_outbreak(chapter_data: dict[int, int], val_to_set: int) -> dict[int, int]:
    """Set a chapter of an outbreak"""

    for level_id in chapter_data.keys():
        chapter_data[level_id] = val_to_set
    return chapter_data


def set_outbreaks(
    outbreaks: dict[int, Any], current_outbreaks: dict[int, Any], ids: list[int]
) -> tuple[dict[int, Any], dict[int, Any]]:
    """Set outbreaks"""

    for chapter_id in ids:
        outbreaks[chapter_id] = set_outbreak(outbreaks[chapter_id], 1)
        if chapter_id in current_outbreaks:
            current_outbreaks[chapter_id] = set_outbreak(current_outbreaks[chapter_id], 0)
    return outbreaks, current_outbreaks


def edit_outbreaks(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for editting outbreaks"""

    outbreaks = save_stats["outbreaks"]["outbreaks"]
    current_outbreaks = save_stats["current_outbreaks"]["outbreaks"]

    available_chapters = get_available_chapters(outbreaks)

    print("What chapter do you want to edit:")
    ids = user_input_handler.select_not_inc(
        options=available_chapters,
        mode="clear the outbreaks for?",
    )
    ids = helper.check_clamp(ids, len(available_chapters)+1, 0, 0)
    ids = main_story.format_story_ids(ids)
    outbreaks, current_outbreaks = set_outbreaks(
        outbreaks, current_outbreaks, ids
    )
    save_stats["outbreaks"]["outbreaks"] = outbreaks
    save_stats["current_outbreaks"]["outbreaks"] = current_outbreaks
    print("Successfully set outbreaks")
    return save_stats
