from flask import flash
from markdown import markdown


def to_html(raw):
    html = markdown(raw, output_format='html',
                    extensions=['markdown.extensions.extra',
                                'markdown.extensions.codehilite'])

    return html


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error)
                  )
