function updateTileJustValue(tileId, data, config, tileType) {
    Tipboard.Dashboard.setDataByKeys(tileId, data, "all");
    Tipboard.Palette.applyFading(document.getElementById("body-" + tileId),
        config.big_value_color, config.fading_background);
}

Tipboard.Dashboard.registerUpdateFunction("just_value", updateTileJustValue);
