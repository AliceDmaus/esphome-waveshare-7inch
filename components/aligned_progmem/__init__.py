# Works around a missing alignment guarantee in ESPHome's core codegen.
#
# ESPHome emits all flash-embedded byte arrays (images, fonts, ...) via
# cg.progmem_array(), which cpp_generator.ProgmemAssignmentExpression renders as
# `static constexpr T name[] PROGMEM = {...}` with no alignment attribute.
#
# LVGL v9 requires image draw buffers to be aligned to LV_DRAW_BUF_ALIGN (32 bytes
# on this board's config). Since the generated arrays aren't aligned, LVGL logs
# "lv_draw_buf_init: Data is not aligned, ignored" on every redraw that touches an
# image and falls back to a slower, unaligned copy path - on this display (single,
# live-scanned PSRAM framebuffer) that extra time widens the window in which a
# redraw can visibly tear.
#
# This patches the array declaration to add alignas(64) (a superset of the 32-byte
# requirement) before ESPHome writes main.cpp. Remove this component once ESPHome
# aligns progmem_array() output upstream.
from esphome.cpp_generator import ProgmemAssignmentExpression
import esphome.config_validation as cv

CONFIG_SCHEMA = cv.Schema({})

_ALIGNMENT = 64

if not getattr(ProgmemAssignmentExpression, "_aligned_progmem_patch", False):

    def _aligned_str(self):
        return f"alignas({_ALIGNMENT}) static constexpr {self.type} {self.name}[] PROGMEM = {self.rhs}"

    ProgmemAssignmentExpression.__str__ = _aligned_str
    ProgmemAssignmentExpression._aligned_progmem_patch = True


async def to_code(config):
    pass
