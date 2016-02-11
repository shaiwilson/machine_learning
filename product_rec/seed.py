 """Utility file to seed training set of images database from image_test_data in seed_data/"""

# from model import Image, Label, connect_to_db, db
from server import app


def load_images():
    """Load images from image_test_data into database."""

    print "Images"

    for i, row in enumerate(open("seed_data/image_id_and_label")):
        row = row.rstrip()
        iamge_id, label = row.split(",")

        image = Image(id=image_id,
                    label=label)

        # We need to add to the session or it won't ever be stored
        db.session.add(image)

        # provide some sense of progress
        if i % 100 == 0:
            print i

    # Once we're done, we should commit our work
    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    # load_images()
