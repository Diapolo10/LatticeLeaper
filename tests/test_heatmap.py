"""Test heatmap functions."""

import pytest

from lattice_leaper.heatmap import filter_heatmap, generate_heatmap, render_heatmap


def test_generate_heatmap_valid(parsed_maze):
    """Test generating a valid heatmap."""
    result = generate_heatmap(parsed_maze, 20)

    assert isinstance(result, dict)


def test_filter_heatmap_valid(parsed_maze):
    """Test filtering a generated heatmap."""
    heatmap = generate_heatmap(parsed_maze, 200)
    filtered = filter_heatmap(heatmap, (20, 28))

    assert isinstance(filtered, dict)


def test_filter_heatmap_distance_too_short(parsed_maze):
    """Test filtering a generated heatmap."""
    result = generate_heatmap(parsed_maze, 20)

    with pytest.raises(ValueError, match="No path between points"):
        filter_heatmap(result, (20, 28))


def test_render_heatmap_valid(parsed_maze):
    """Test rendering a heatmap."""
    heatmap = generate_heatmap(parsed_maze, 200)
    filtered = filter_heatmap(heatmap, (20, 28))
    result = render_heatmap(parsed_maze, filtered, 2)

    assert isinstance(result, str), result
    assert result.startswith('  \x1b[36;49m#'), result
