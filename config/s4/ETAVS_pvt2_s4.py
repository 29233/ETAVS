model = dict(
    type='AVS_Model',
    backbone=dict(
        type='pvt_v2_b5',
        init_weights_path='pretrained/pvt_v2_b5.pth'),
    vggish=dict(
        freeze_audio_extractor=True,
        pretrained_vggish_model_path='pretrained/vggish-10086976.pth',
        preprocess_audio_to_log_mel=False,
        postprocess_log_mel_with_pca=False,
        pretrained_pca_params_path=None),
    bridger=dict(
        type='TemporalFusers',
        nhead=8,
        t=5,
        num_queries=5,
        dropout=0.1,
        feature_channel=[64, 128, 320, 512],
    ),
    head=dict(
        type='RefFormerHead',
        scale_factors=[8, 4, 2, 1],
        d_models=[64, 128, 320, 512],
        nhead=8,
        pos_emb=None,
        drop_out=0.1,
        conv_dim=256,
        mask_dim=1,
        use_bias=False,
        interpolate_scale=4
    ),
    freeze=dict(
        audio_backbone=True,
        visual_backbone=True
    )
)
dataset = dict(
    train=dict(
        type='S4Dataset',
        split='train',
        anno_csv='/18018998051/data/Single-source/s4_meta_data.csv',
        dir_img='/18018998051/data/Single-source/s4_data/visual_frames',
        dir_audio_log_mel='/18018998051/data/Single-source/s4_data/audio_log_mel',
        dir_mask='/18018998051/data/Single-source/s4_data/gt_masks',
        img_size=(224, 224),
        batch_size=4),
    val=dict(
        type='S4Dataset',
        split='test',
        anno_csv='/18018998051/data/Single-source/s4_meta_data.csv',
        dir_img='/18018998051/data/Single-source/s4_data/visual_frames',
        dir_audio_log_mel='/18018998051/data/Single-source/s4_data/audio_log_mel',
        dir_mask='/18018998051/data/Single-source/s4_data/gt_masks',
        img_size=(224, 224),
        batch_size=4),
    test=dict(
        type='S4Dataset',
        split='test',
        anno_csv='/18018998051/data/Single-source/s4_meta_data.csv',
        dir_img='/18018998051/data/Single-source/s4_data/visual_frames',
        dir_audio_log_mel='/18018998051/data/Single-source/s4_data/audio_log_mel',
        dir_mask='/18018998051/data/Single-source/s4_data/gt_masks',
        img_size=(224, 224),
        batch_size=4))
optimizer = dict(
    type='AdamW',
    lr=6e-5)
loss = dict(
    weight_dict=dict(
        dice_loss=1.0,
        focal_loss=0.0),
    loss_type='dice')
process = dict(
    num_works=8,
    freeze_epochs=-1,
    train_epochs=30)
discribe = dict(
    session_name='S4',
    info='ETAVS_pvt2_S4'
)
