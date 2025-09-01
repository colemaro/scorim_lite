from flask import render_template, redirect, url_for, flash, send_from_directory, request, send_file, Response

import os

from app import app

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.route('/placeholder')
def placeholder():
    return render_template('placeholder.html')

@app.route('/')
@app.route('/main')
def main():
    # Function needs to get all of the images in images and sort them
    # needs to create a pagination object.. 
    image_order_dict = {}
    for root, dirs, files in os.walk(app.config['CREATOR_IMAGE_FOLDER']):
        for file in files:
            order_num = int(os.path.basename(os.path.normpath(root)))
            image_order_dict[order_num] = f"/serve_single_dicom/{order_num}/{file}"
            
    sorted_images = sorted(image_order_dict.items())
    per_page = 2
    
    page = int(request.args.get("page", 1))
    
    start = (page - 1) * per_page
    end = start + per_page
    
    page_items = sorted_images[start:end]
    
    has_prev = page > 1
    has_next = end < len(sorted_images)
    
    return render_template("two_im_scoring.html", page=page, page_items=page_items, has_prev=has_prev, has_next=has_next)

@app.route('/serve_single_dicom/<order>/<filename>')
def dicom_file(order, filename):
    order_as_direction = f"{int(order):003}"
    image_directory = os.path.join(app.config['CREATOR_IMAGE_FOLDER'])
    mid_point = os.path.join(image_directory, order_as_direction)
    dicom_path = os.path.join(mid_point, filename)
    return send_file(dicom_path, as_attachment=False)